//handling many errors
try:
	a=int(input("enter a:"))
	b=int(input("enter b:"))
	ans=a/b
	print(ans)
	assert a>1
	print(x)
except assertionerror as e:
	print("error")
except nameerror as e:
	print("error!";e)
except exception as e:
	print(e)