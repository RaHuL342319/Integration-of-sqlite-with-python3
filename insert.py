import sqlite3
# to connect to an existing database.
# If the database does not exist,
# then it will be created and finally a database object will be returned.
conn = sqlite3.connect('test.db')
print("Opened database successfully")


# inserting data to Movies table

conn.execute("INSERT INTO Movies (NAME,Actor,Actress,Director,Year_Of_Release) \
      VALUES ('Iron Man', 'Robert Downey Jr.', 'Gwyneth Paltrow','Jon Favreau', 2008 )")

conn.execute("INSERT INTO Movies (NAME,Actor,Actress,Director,Year_Of_Release) \
      VALUES ('Shershaah', 'Shiddarth Malhotra', 'Kiara Advani','Vishnuvardhan', 2021 )")

conn.execute("INSERT INTO Movies (NAME,Actor,Actress,Director,Year_Of_Release) \
      VALUES ('Mimi', 'Pankaj Tripathi', 'Kriti Sanon','Laxman Utekar', 2021 )")

conn.execute("INSERT INTO Movies (NAME,Actor,Actress,Director,Year_Of_Release) \
      VALUES ('Iron Man 2', 'Robert Downey Jr.', 'Gwyneth Paltrow','Jon Favreau', 2008 )")

conn.execute("INSERT INTO Movies (NAME,Actor,Actress,Director,Year_Of_Release) \
      VALUES ('Ek Villain',  'Shiddarth Malhotra', 'Shraddha Kapoor','Mohit Suri', 2014 )")

conn.commit()
print("Records created successfully")
