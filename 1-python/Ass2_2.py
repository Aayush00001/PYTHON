2.Write a python program to read N bytes from a file.( N must be entered by the user.)
	some_bytes = b'\x21'
	binary_file = open("D:\COLLAGE\SEM4\DS\Ass2.txt", "wb")
	binary_file.write(some_bytes)
	binary_file.close()
