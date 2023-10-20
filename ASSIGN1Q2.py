#4] Write a Python function to find the maximum of three numbers.


a,b,c = input("enter three numbers").split()

if a>b:
	if a>c:
		print(f"a is greater")
elif b>c:
	print(f"b is greater")
else:
	print(f"c is greater")
