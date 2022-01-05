b= set()
print(type(b))

#adding values to an empty set
b.add(4)
b.add(5)
b.add(7)
b.add(4) #adding value repeatedly does not change a set
print(b)
b.add((9,8,3,1))
# b.add({4:5}) #cannot add list or dictionary
print(b)

print(len(b)) #prints lenth of this set
b.remove(5)
print(b)