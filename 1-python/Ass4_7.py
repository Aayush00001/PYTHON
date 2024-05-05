//Write a python program to alter the employee table and add a new column “DateOfJoin”.
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
mycursor=con.cursor()
mycursor.execute("ALTER TABLE Persons ADD DateOfBirth date;")
con.commit()
con.close()