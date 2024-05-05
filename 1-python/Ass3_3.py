//Write a python program to extract Date from a given text file.
//(Date Format : DD/MM/YYYY)
import re
f=open("D:/readdata.txt",'r')
data=f.read()
ans=re.findall(r'(\d+/\d+/\d+)',data)
print(ans)
          