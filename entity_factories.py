from entity import Entity

player = Entity(char="@", color=(255, 255, 255), eyesight_radius=8, name="Player", blocks_movement=True)

orc = Entity(char="o", color=(63, 127, 63), eyesight_radius=8, name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 127, 0), eyesight_radius=9, name="Troll", blocks_movement=True)