import sqlite3

connection = sqlite3.connect('collyers_car_park.db')

cursor = connection.cursor()

# create details table
details_table = """CREATE TABLE IF NOT EXISTS
details(
user_id INTEGER PRIMARY KEY
);"""
cursor.execute(details_table)
details_default_values = [(1,),(2,),(3,),(4,),(5,)] # <---- single value tuples

cursor.executemany("INSERT INTO details (user_id) VALUES (?)", details_default_values)
connection.commit()

latest_id = cursor.execute("""SELECT * FROM details""")
print(latest_id.fetchall())