"""Pomocí sqlite3 modulu v python udělejte následujcí dotazy:

1) z db chinook.db vyberte 3 nejdelší skladby z tabulky tracks
- získejte data a vyprintujete
2) updatuje záznamy z tabulky artists
- nastavte name na hodnotu 'Moje kapela', kde name je 'Test'

odevzdejte jako 25_sqlite.py


přikládám db diagram
https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf"""




import sqlite3
conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()

query = "SELECT name, Milliseconds FROM tracks ORDER BY Milliseconds DESC LIMIT 3"  

cursor.execute(query)
tri_nejdelsi = cursor.fetchall()
print(tri_nejdelsi)

query = "UPDATE artists SET name = 'Moje kapela' WHERE name = 'Test'"
cursor.execute(query)

conn.commit()