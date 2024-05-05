//exception handling with orignak error
try:
	a=int(input("enter a:"))
	b=int(input("enter b:"))
	ans=a/b
	print(ans)
except exception as e:
	print(e)
else:
	print("no error occured!!")
finally:
	print("execution completed!!")