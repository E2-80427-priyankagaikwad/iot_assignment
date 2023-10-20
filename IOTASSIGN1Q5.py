#)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
#ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
#Average Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F



a =int( input("enter math subject marks"))
b = int( input("enter science subject marks"))
c= int( input("enter marathi subject marks"))


r = (a+b+c)/3

if 90 <= r <= 100:
	print("congratulations you got grade A")
elif 80<= r <= 89:
	print(" you have got grade B")
elif 70 <= r <=79:
	print("you have got grade C")
elif 60 <= r <=69:
	print("you have got grade D")
else:
	print(" study hard ! you got grade F")
