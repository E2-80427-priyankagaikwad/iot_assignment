#6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
#epts the number as an argument.

def fact(num):
	i=1
	r=num
	while i<num:
		r *= i
		i= i+1
	print(f"fact is {r}")
	

a=int(input("enter number"))
fact(a)	








"""def fact(i):
	n = int (input("enter number"))
	result=1
	while n>0:
		result *= n
		n -= 1
	print(f"fact{result}")

fact(5)"""
