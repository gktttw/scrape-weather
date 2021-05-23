import sqlite3 as sl

con = sl.connect('cwb.db')

with con:
    con.execute("""
        CREATE TABLE WEATHER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            city_name TEXT,
            date TEXT,
            time TEXT,
            temperature TEXT,
            status TEXT
        );
    """)
