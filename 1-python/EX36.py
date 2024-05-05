//fetchong a data from atable in mysql using python
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="collage")
a=con.cursor()
a.execute("CREATE TABLE dept2(first_name VARCHAR (50),last_name VARCHAR(50));")
results=a.fetchone()
print(results)
con.close()
