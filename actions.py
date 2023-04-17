from __future__ import annotations

from random import Random
from typing import Optional, Tuple, TYPE_CHECKING

import colors
import exceptions
from components.skills import SkillEnum

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item


class Action:
    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity
        self.rand_generator = Random()

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to"""
        return self.entity.gamemap.engine

    def perform(self) -> None:
        raise NotImplementedError()

class ItemAction(Action):
    def __init__(self, entity: Actor, item: Item, target_xy: Optional[Tuple[int, int]] = None):
        super().__init__(entity)
        self.item = item
        if not target_xy:
            target_xy = entity.x, entity.y
        self.target_xy = target_xy

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination"""
        return self.engine.game_map.get_actor_at_location(*self.target_xy)

    def perform(self) -> None:
        """Invoke the items' ability, this action will be given to provide context."""
        if self.item.consumable:
            self.item.consumable.activate(self)


class DropItemAction(ItemAction):
    def perform(self) -> None:
        if self.entity.equipment.item_is_equipped(self.item):
            self.entity.equipment.toggle_equip(self.item)

        self.entity.inventory.drop(self.item)


class EquipAction(Action):
    def __init__(self, entity: Actor, item: Item):
        super().__init__(entity)

        self.item = item

    def perform(self) -> None:
        self.entity.equipment.toggle_equip(self.item)


class WaitAction(Action):
    def perform(self) -> None:
        pass


class TakeStairsAction(Action):
    def perform(self) -> None:
        """Take the stairs, if any exist at the entity's location"""
        if (self.entity.x, self.entity.y) == self.engine.game_map.downstairs_location:
            self.engine.game_world.generate_floor()
            self.engine.message_log.add_message("You descend the staircase", colors.DESCEND)
        else:
            raise exceptions.Impossible("there are no stairs here")

class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Retruns this action's destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this action's destination."""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination"""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()


class MeleeAction(ActionWithDirection):
    def perform(self) -> None:
        target = self.target_actor
        if not target:
            raise exceptions.Impossible("Nothing to attack")

        chance_to_hit = self.entity.fighter.hit_rate() - target.fighter.evasion()
        attack_role = self.rand_generator.randint(1, 100)
        if attack_role <= chance_to_hit:
            # The attack hit, calculate damage
            enemy_armor_rating = target.fighter.armor_rating()
            print(f"Enemy armor rating: {enemy_armor_rating}")
            damage = self.entity.fighter.damage(enemy_armor_rating)
            target.fighter.take_damage(damage)
            attack_desc = f"{self.entity.name.capitalize()} attacks {target.name}"
            if self.entity is self.engine.player:
                attack_color = colors.PLAYER_ATTACK
            else:
                attack_color = colors.ENEMY_ATTACK
            if damage > 0:
                self.engine.message_log.add_message(f"{attack_desc} for {damage} hit points.", attack_color)
                target.primary_attributes.health -= damage
            else:
                self.engine.message_log.add_message(f"{attack_desc} but does no damage.", attack_color)
        else:
            self.engine.message_log.add_message(f"{target.name} dodged out of the way!", colors.HEALTH_RECOVERED) # TODO: Get a better color


class MovementAction(ActionWithDirection):

    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            raise exceptions.Impossible("That way is blocked") # the target is out of bounds, don't do anything
        if not self.engine.game_map.tiles["walkable"][dest_x][dest_y]:
            raise exceptions.Impossible("You can't walk there!")

        possible_blocking_entity = self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if possible_blocking_entity:
            raise exceptions.Impossible(f"You've bumped into {possible_blocking_entity.name}") # Destination blocked by entity

        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self) -> None:
        if self.target_actor:
            if self.engine.player.skills.skill_map[SkillEnum.HAND_TO_HAND][1] == 0:
                print("Found you!")
            return MeleeAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


class PickupAction(Action):
    """Pickup an item and add it to the inventory, if there is room for it"""
    def __init__(self, entity: Actor):
        super().__init__(entity)

    def perform(self) -> None:
        actor_location_x, actor_location_y = self.entity.x, self.entity.y
        inventory = self.entity.inventory

        for item in self.engine.game_map.items:
            if actor_location_x == item.x and actor_location_y == item.y:
                if len(inventory.items) >= inventory.capacity:
                    raise exceptions.Impossible("Your inventory is full")

                self.engine.game_map.entities.remove(item)
                item.parent = self.entity.inventory
                inventory.items.append(item)

                self.engine.message_log.add_message(f"You picked up the {item.name}")
                return

        raise exceptions.Impossible("There is nothing here to pick up.")
