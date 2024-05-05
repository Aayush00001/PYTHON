3.Write a python program to write data entered by the user in a file.
	temp =input("Please enter your information!!   ")
	try:
    with open('D:\COLLAGE\SEM4\DS\Ass2.txt',"w") as Ass2:
    Ass2.write(temp)
	except Exception as e:
    print("There is a Problem", str(e))
	