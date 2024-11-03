import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "How_1metyourmother",
    database = "test_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 2")

myresult =mycursor.fetchall()

for result in myresult:
    print (result)

#UPDATING OUR TABLE DATA
# sql = "UPDATE students SET age = 15 WHERE name = 'Bob'"

# mycursor.execute(sql)

# mydb.commit()



#TO SELECT AND GET DATA FROM TABLES
# mycursor.execute("SELECT * FROM students")

# myresult = mycursor.fetchmany()

# for row in myresult:
#     print(row) 



#TO INPUT DATA IN THE TABLES
# sqlformula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Bob", 22),
#             ("Ruth", 22),
#             ("Daniel", 22),
#             ("Peter", 22),
#             ("Jonah", 22),]

# mycursor.executemany(sqlformula, students)

# mydb.commit()