with open('sample1.txt') as f:
    content= f.read()

content= content.replace('avi', "ytgjuuy")

with open('sample1.txt', 'w') as f:
    f.write(content)