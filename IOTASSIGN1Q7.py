#7) Using for loop, write and run a Python program to find factorial from 0 to 10.

def fact(num):
	i=1
	r=num
	while i<num :
		r *= i
		i= i+1
	print(f"fact is {r}")
  
  
 #a=int(input("enter number"))
collection = [0,1,2,3,4,5,6,7,8,9,10]  
for i in collection:
	if i==0:
		print("fact is 1")
	else:
		fact(i) 
