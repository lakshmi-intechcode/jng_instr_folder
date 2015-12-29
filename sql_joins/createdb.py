import sqlite3

db = sqlite.connect('livingdb')

cursor = db.cursor()

cursor.execute('''
	CREATE TABLE buildings(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		city TEXT,
		build_year INTEGER
	);
''')

cursor.execute('''
	CREATE TABLE residents(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name TEXT,
		last_name TEXT,
		rent INTEGER,
		building_id INTEGER,
		FOREIGN KEY(building_id) AS buildings(id)
	);
''')

db.commit()
db.close()

