num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if num1<num2:
    if num2<num3:
        print("the greatest number is ", num3)
    else:
        print("the greatest number is ", num2)

else:
    if num1<num3:
        print("the greatest number is ", num3)
    else:
        print("the greatest number is ", num1)



def maximum(num1, num2, num3):
    if num1<num2:
        if num2<num3:
            return num3
        else:
            return num2
    else:
        if num1<num3:
            return num3
        else:
            return num1

s= maximum(12,20,56)
print(s)

