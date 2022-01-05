marks = int(input('Enter your marks'))
a = marks

if (a>90):
    grade = "Ex"
elif(a>80):
    grade = "A+"
elif(a>70):
    grade = "A"
elif(a>60):
    grade = "B"
elif(a>50):
    grade = "C"
elif(a>=40):
    grade = "D"
else:
    print("Sorry your fail in exam")
print('your grade is', grade)
