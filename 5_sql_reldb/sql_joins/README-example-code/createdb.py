import sqlite3

db = sqlite3.connect('livingdb')

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE buildings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        build_year INTEGER
    );
''')

db.commit()

cursor.execute('''
    CREATE TABLE residents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        rent INTEGER,
        building_id INTEGER,
        FOREIGN KEY(building_id) REFERENCES buildings(id)
    );
''')

db.commit()
db.close()