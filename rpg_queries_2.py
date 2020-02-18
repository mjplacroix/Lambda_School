
# How many total Characters are there?
SELECT
    COUNT(character_id)
FROM
    charactercreator_character

# How many of each specific subclass?
SELECT
    COUNT(DISTINCT charactercreator_mage.character_ptr_id) AS MageCount,
    COUNT(DISTINCT charactercreator_thief.character_ptr_id) AS ThiefCount,
    COUNT(DISTINCT charactercreator_cleric.character_ptr_id) AS ClericCount,
    COUNT(DISTINCT charactercreator_fighter.character_ptr_id) AS FighterCount
FROM
    charactercreator_mage,
    charactercreator_thief,
    charactercreator_cleric,
    charactercreator_fighter

# How many total Items?
items = 
SELECT
	COUNT(item_id)
FROM armory_item
	
# How many of the Items are weapons? How many are not?
weapons = SELECT COUNT(item_ptr_id) AS Weapons FROM armory_weapon;
not_weapons = items - weapons
# # attempts
# SELECT item_ptr_id, COUNT(item_id) AS Not_Weapons
# FROM armory_weapon, armory_item


# SELECT COUNT(item_id) AS Not_Weapons
# FROM armory_item
# WHERE item_id NOT IN:
# 	SELECT item_ptr_id 
# 	FROM armory_weapon


# How many Items does each character have? (Return first 20 rows)
SELECT
    character_id,
    COUNT(DISTINCT item_id) as Items
FROM
    charactercreator_character_inventory
GROUP BY
    character_id
LIMIT
    20

# How many Weapons does each character have ? (Return first 20 rows)
SELECT
    charactercreator_character_inventory.character_id,
    COUNT(
        DISTINCT charactercreator_character_inventory.item_id
    ) AS Weapons
FROM
    charactercreator_character_inventory
    JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY
    charactercreator_character_inventory.character_id
LIMIT
    20


# On average, how many Items does each Character have?
SELECT
    AVG(Items)
FROM
    (
        SELECT
            character_id,
            COUNT(DISTINCT item_id) as Items
        FROM
            charactercreator_character_inventory
        GROUP BY
            character_id
    )


# On average, how many Weapons does each character have?
SELECT
    AVG(Weapons)
FROM
    (
        SELECT
            charactercreator_character_inventory.character_id,
            COUNT(
                DISTINCT charactercreator_character_inventory.item_id
            ) AS Weapons
        FROM
            charactercreator_character_inventory
            JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
        GROUP BY
            charactercreator_character_inventory.character_id
    )