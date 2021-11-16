import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="*********",
  database="Todo"
)

mycursor = mydb.cursor()

# mycursor.execute("show tables;")
# for x in mycursor:
#   print(x)

mycursor.execute("""CREATE TABLE items 
(item varchar(255)  NOT NULL, 
status varchar(255) NOT NULL, 
PRIMARY KEY(item) );""")
