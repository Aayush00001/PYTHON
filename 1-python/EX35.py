import mysql.connector as c
con=c.connect(host="localhost",user="root",password="")
print(con)
c1=con.cursor()
c1.execute("create database collage;")
con.close
