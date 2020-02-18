import os
import sqlite3

# database path
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = """
SELECT
    COUNT(character_id)
FROM
    charactercreator_character
"""
result = cursor.execute(query).fetchall()
print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)


#result2 = cursor.execute(query).fetchall()