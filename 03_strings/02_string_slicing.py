name = "avinash"
b = "is very good boy."

print(name+b)

print(name[-7]) #printed the letter which is 1st place that is a
# print(name[-1]) #printe the letter last letter ie. h
# print(name[2])
# print(name[3])
print(name[-2])

print(name[0:3]) #print the letter avi
print(name[-7:-1]) #print letter aninas
print(name[-7:])    #print letter avinash
print(name[1:4]) # print letter vin
print(name[-4:-1]) # print letter nas

print(b[1::3]) #print every 3rd latter
print(b[-17]) # print first letter
print(len(b)) #print how many string are there= 17 

print(b.endswith("boy.")) #string ended with that letter if yes then true otherwise false
print(b.count('o'))      # count letter how many times appear
print(b.capitalize())     #capitalize fist letter
print(b.find("very"))   #find number of first letter of string
print(b.replace('good', "bad")) # replace good with bad
