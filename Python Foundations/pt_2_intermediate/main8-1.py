# database programming
import sqlite3

connection = sqlite3.connect('mydata.db') # database name
cursor = connection.cursor()

class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first_name = first
        self.last_name = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db') # database name
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute(f"SELECT * FROM persons WHERE id={id_number}")
        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first_name = results[1]
        self.last_name = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute(f'INSERT INTO persons VALUES ({self.id_number},"{self.first_name}","{self.last_name}",{self.age})')
        self.connection.commit()


# creating local database, table, and entries
# connection = sqlite3.connect('mydata.db') # database name
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, first_name TEXT,last_name TEXT,age INTEGER)")
# cursor.execute("INSERT INTO persons VALUES (1, 'Paul', 'Smith', 24), (2, 'Mark', 'Johnson', 42), (3, 'Anna', 'Smith', 34)")
# cursor.execute("SELECT * FROM persons WHERE last_name='Smith'")
# rows = cursor.fetchall()
# print(rows)
# connection.commit()
# connection.close()


# creating a python object using database data
# p1 = Person()
# p1.load_person(1)
# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)
# print(p1.id_number)

# creating a database entry using python
# p1 = Person(7, "Anna", "Robbins", 30)
# p1.insert_person()


# connection = sqlite3.connect('mydata.db') # database name
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM persons')
# results = cursor.fetchall()
# print(results)

# connection.close()


# loading created user using python object
p2 = Person()
p2.load_person(7)
print(p2.first_name)
print(p2.last_name)
print(p2.age)
print(p2.id_number)
