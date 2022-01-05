with  open('copy.txt', 'r') as f:  #close atomatic with fuction
    a= f.read()
with open('copy.txt', 'w') as f:
    a= f.write("ok i have done")
print(a)

