//Write a python program to delete employees who belong to the computer department and count how many rows are affected.import mysql.connector as c
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
mycursor=con.cursor()
mycursor.execute("DELETE FROM employees WHERE department=computer")
con.commit()
print(mycursor.rowcount,"rows affected")
con.close()