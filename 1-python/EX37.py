//insert into progrma
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="collage")
a=con.cursor()
a.execute("insert into dept2 values('aayush','soni');")
con.commit()
con.close()
