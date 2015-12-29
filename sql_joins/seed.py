"""
SEED YOUR TABLES
"""

import sqlite3
import pdb

db = 'livingdb'

BUILDINGS =[
	[],
	[],
	[],
]

RESIDENTS = [
	[],
	[],
	[],
]

conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM buildings")
c.execute("DELETE FROM residents")

for building in BUILDINGS:
	c.execute("""
		INSERT INTO buildings ("name", "city", "build_year") VALUES (?, ?, ?)""",('put values in here'))

conn.commit()

for resident in RESIDENTS:
	c.execute("""
		INSERT INTO residents ("first_name", "last_name", "residents") VALUES (?, ?, ?)""",('put in the values here'))

conn.commit()

c.close()

print("SEEDED")

