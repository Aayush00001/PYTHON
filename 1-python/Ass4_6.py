//Write a python program to update the salary of all employees by 5%.
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
mycursor=con.cursor()
mycursor.execute("UPDATE employee SET salary= salary + (salary * 5 / 100) WHERE salary > 4000;")
con.commit()
con.close()