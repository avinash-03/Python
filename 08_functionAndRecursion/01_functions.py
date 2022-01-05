def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400*100)
    return p

marks1 = [48, 54, 76, 62]
percentage1= percent(marks1)

marks2 = [44, 16, 72, 64]
percentage2= percent(marks2)

print(percentage1, percentage2)