a = input("Enter your setence to verify\n")

if("make a lot money" in a):
    spam=True
elif("buy now" in a):
    spam=True
elif("subscribe now" in a):
    spam=True
elif("click this" in a):
    spam=True
else:
    spam=False

if(spam):
    print("this is spam")
else:
    print("this is not spam")