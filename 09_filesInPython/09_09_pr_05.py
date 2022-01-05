with open('sample1.txt') as f:
    content= f.read()

words= ['is', 'name', 'very']

for word in words:
    content= content.replace(word, "ghik")
    with open('sample1.txt', 'w') as f:
        f.write(content)