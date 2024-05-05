//delete program
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="collage")
a=con.cursor()
a.execute("delete from dept2 where first_name=aayush;")
con.commit()
print(a.rowcount,"rows affected;")
con.close()
