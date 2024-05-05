//Write a python program to create a table named “EMPLOYEE” that contains following columns:
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
a=con.cursor()
a.execute("create table employee(Emp_ID Int(10),Emp_Name varchar(20),City varchar(20),Salary Int(20),Department varchar(20),Designation varchar(20));")
con.close()
