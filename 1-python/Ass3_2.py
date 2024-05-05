//Write a python program to extract contact No. from a given text file.
import re
f=open("D:\readdata.txt",'r')
data=f.read()
ans=re.findall(r'\b\d{10}\b',data)
print(ans)

