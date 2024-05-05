//Write a python program to fetch all the data from the employee table.
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
a=con.cursor()
a.execute("SELECT * FROM employee")
myresult=a.fetchall()
for x in myresult:
  print(x)
