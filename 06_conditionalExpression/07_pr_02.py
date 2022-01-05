s1 = int(input('enter your mark for sub1='))
s2 = int(input('enter your mark for sub2='))
s3 = int(input('enter your mark for sub3='))

if(s1<33 or s2<33 or s3 < 33):
    print("you are failed because one of the subject have less than 33%")
elif(s1+s2+s3/3 < 40):
    print('Your are failed because total marks have less than 40%')
else:
    print("congratulation You are pass in exam")


