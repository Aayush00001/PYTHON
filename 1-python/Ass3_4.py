//Write a python program to count the number of vowels in a text file.
import re
f=open("D:/readdata.txt",'r')
data=f.read()
ans=re.findall(r'[a,e,i,o,u]',data)
result=len(ans)
print(result)