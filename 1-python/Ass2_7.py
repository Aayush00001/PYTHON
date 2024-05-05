7.Write a python program to write a list to a file.
	names=['APPLE', 'MANGO', 'CHERRY']
	with open(r'D:\COLLAGE\SEM4\DS\Ass2.txt', 'w') as fp:
   	for item in names:
    fp.write("%s\n" % item)
