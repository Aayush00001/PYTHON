//Write a python program to extract email-ids from a text file.
import re
f=open("d:/readdata.txt","r")
data=f.read()
ans=re.findall(r'\S+@\S+',data)
print(ans)