//Write a python program to check whether every string ends with ‘ . ’(dot) or not in a text file.
import re
f=open("D:/readdata.txt",'r')
data=f.read()
ans=re.findall('.$',data)
print(ans)
