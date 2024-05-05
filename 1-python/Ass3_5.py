//Write a python program to retrieve all words having 5 characters length from a text file.
import re
f=open("D:/readdata.txt",'r')
data=f.read()
ans=re.findall(r'\b\w{5}\b',data)
print(ans)
