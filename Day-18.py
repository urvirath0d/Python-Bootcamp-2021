import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="BESTENLIST"
)
print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE DOCTORS")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)



dbse.execute("CREATE TABLE DOCTORS (dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
('doctors',)
dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_id , Patient_visited) VALUES (%s,%s)"
val = [
    ('Dr1','9'),
    ('Dr2','3'),
    ('Dr3','8'),
    ('Dr4','0'),
    ('Dr23','5'),
    ('Dr26','9'),
    ('Dr8','0'),
    ('Dr5','0'),
    ('Dr13','5'),
    ('Dr62','9'),
    ('Dr83','0')
]

dbse.executemany(sql, val)

mydb.commit()


#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harsha27",
  database="DOCTOR"
)
dbse = mydb.cursor()
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harsha27",
  database="DOCTOR"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


