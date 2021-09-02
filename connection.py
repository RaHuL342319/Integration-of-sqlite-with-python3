import sqlite3
# to connect to an existing database.
# If the database does not exist,
# then it will be created and finally a database object will be returned.
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# to create a table named "Movies"in test.db database
conn.execute('''CREATE TABLE Movies
         (
         NAME   TEXT    NOT NULL,
         Actor  TEXT,
         Actress    TEXT,
         Director   TEXT    NOT NULL,
          Year_Of_Release   INT
         );''')


print("Created Table Movies Successfully!!")
