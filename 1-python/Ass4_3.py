//Write a python program to insert 5 records in the above table. (values must be taken from user)
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="AAYUSH")
aa=con.cursor()
Emp_ID=int(input("enter id"))
Emp_Name=str(input("enter name"))
City=str(input("enter city"))
Salary=int(input("enter salary"))
Department=str(input("enter department"))
Designation=str(input("enter desgination"))
aa.execute("INSERT INTO employee(Emp_ID,Emp_Name,City,Salary,Department,Designation) VALUES ({},'{}','{}',{},'{}','{}')".format(Emp_ID,Emp_Name,City,Salary,Department,Designation))
con.commit()
con.close()

