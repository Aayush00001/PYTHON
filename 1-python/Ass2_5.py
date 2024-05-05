5.Write a python program to count the number of characters(excluding space) in a text file.
	file = open("D:\COLLAGE\SEM4\DS\Ass2.txt", "r")
	data = file.read()
	number_of_characters = len(data)
	print('Number of characters in text file :', number_of_characters)
	