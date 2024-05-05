import mysql.connector as c
con=c.connect(host="localhost",user="root",password="")
print(con)
con.close