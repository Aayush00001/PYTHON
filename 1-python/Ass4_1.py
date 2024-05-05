//Write a python program to create a database  “MYDATABASE”  in phpmyadmin.
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="")
print(con)
c1=con.cursor()
c1.execute("create database AAYUSH")
con.close()