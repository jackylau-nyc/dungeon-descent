from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="&",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=1),
    inventory=Inventory(capacity=9),
    level=Level(level_up_base=100),
)

goblin = Actor(
    char="g",
    color=(63, 127, 63),
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

orc = Actor(
    char="o",
    color=(0, 127, 0),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=1, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

ogre = Actor(
    char="O",
    color=(0, 80, 0),
    name="Ogre",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=20, base_defense=2, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200),
)

confusion_scroll = Item(
    char="?",
    color=(255, 255, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="!",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)


health_potion = Item(
    char="u",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=5),
)

mega_potion = Item(
    char="U",
    color=(127, 0, 255),
    name="Mega Potion",
    consumable=consumable.HealingConsumable(amount=15),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=21, maximum_range=5),
)

stick = Item(
    char="/", color=(0, 191, 255), name="Stick", equippable=equippable.Stick()
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(
    char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword()
    )

padded_clothes = Item(
    char="H",
    color=(139, 139, 19),
    name="Padded Clothes",
    equippable=equippable.PaddedClothes(),
)

leather_armor = Item(
    char="H",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="H", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)