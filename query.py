import sqlite3
# to connect to an existing database.
# If the database does not exist,
# then it will be created and finally a database object will be returned.
conn = sqlite3.connect('test.db')
print("Opened database successfully")


# SELECTING WHOLE TABLE
cursor = conn.execute(
    "SELECT * from Movies")
for row in cursor:
    print("Name:", row[0])
    print("Actor:", row[1])
    print("Actress:", row[2])
    print("Director:", row[3])
    print("Year_Of_Release:", row[4])
    print()

# querying based on actor name
cursor = conn.execute(
    "SELECT * FROM Movies WHERE Actor='Shiddarth Malhotra'")
for row in cursor:
    print("Name:", row[0])
    print("Actor:", row[1])
    print("Actress:", row[2])
    print("Director:", row[3])
    print("Year_Of_Release:", row[4])
    print()
