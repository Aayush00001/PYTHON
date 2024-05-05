//Write a python program to verify whether a entered password is valid or not.
//(Valid Password : Having A-Z, a-z, special characters and length between 8-22)
import re
f=str(input("Enter password:"))
if(re.findall(r'\S{8,22}',f)):
    print("valid")
else:
    print("Invalid")
    