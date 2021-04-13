"""sqlite3 examples"""

import sqlite3
import 
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


TOTAL_CHARACTERS = "SELECT * FROM charactercreator_character;"
"""Returns total number of characters"""
curs.execute(TOTAL_CHARACTERS;)
curs.fetchall()

TOTAL_SUBCLASS = "SELECT COUNT(character_id) FROM charactercreator_character"
"""Returns total number of subclasses"""
curs.execute(TOTAL_SUBCLASS)
curs.fetchall()

TOTAL_ITEMS = "SELECT COUNT(name) FROM armory item;"
"""Returns total number of items"""
curs.execute(TOTAL_ITEMS)
curs.fetchall()

WEAPONS = "SELECT * FROM armory_weapon;"
"""Returns all weapons"""
curs.execute(WEAPONS)
curs.fetchall()

NON_WEAPONS = "COUNT(TOTAL_ITEMS) - COUNT(WEAPONS);"
"""Returns count of non weapons"""
curs.execute(NON_WEAPONS)
curs.fetchall()

CHARACTER_ITEMS = "SELECT character_id AND item_id FROM charactercreator_character_inventory INNER JOIN charactercreator_character ON character_id, LIMIT 20;"
"""Returns number of character items"""
curs.execute(CHARACTER_ITEMS)
curs.fetchall()

CHARACTER_WEAPONS = "SELECT item_ptr_id FROM armory_weapon INNER JOIN charactercreator_character_inventory ON item_id, LIMIT 20;"
"""Returns character's weapons"""
curs.execute(CHARACTER_WEAPONS)
curs.fetchall()

AVG_CHARACTER_ITEMS = "COUNT(CHARACTER_ITEMS) / len(TOTAL_CHARACTERS;)"
"""Returns average number of character items.
curs.execute(AVG_CHARACTER_ITEMS)
AVG_CHARACTER_WEAPONS = "COUNT(CHARACTER_WEAPONS) / len(TOTAL_CHARACTERS;)"
"""Returns average number of character_items"""



