mydict = {
    "Fast": "In a Quick Manner",
    "Avi": "A coder",
    "Marks": [1, 2, 3, 4],
    "anotherdict": {'AVo': 'Player'},
    1:2
}
print(list(mydict.keys()))   #prints the keys of the dictionary

print(mydict.values())     #prints values of the dictionay
print(mydict.items())     #prints (keys,values)
print(mydict)
updateDict = {
    "lovish": "friend",
    "divya": "pooja"
}
mydict.update(updateDict)  #pudates the dictionary by adding key-value pairs
print(mydict)

#print(mydict.get('Avi2'))  #Returns None as avi2 is not present in the dictionary
#print(mydict['Avi2'])    #throws an error as avi2 is not present in the dictionary