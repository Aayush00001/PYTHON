//Write a python program to drop the employee table.
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=con.cursor()
mycursor.execute("DROP TABLE student;")
con.commit()
con.close()
