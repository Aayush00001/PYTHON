//Write a python program to read data from the text file and list all the words starting with ‘ s ’.
import re
f=open("D:/collage/sem4/ds/readdata.txt","s")
data=f.read()
ans=re.findall('s\w+',data)
print(ans)