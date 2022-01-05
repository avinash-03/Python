a = {
    "ja": "go",
    'jaldi': "fast",
    "ghar": "home",
    "phir": 'again',
    'so ja': 'sleep'
}
print("my option is ", a.keys())

b = input("Enter one hindi word\n")
#print('the meaning of your word is', a[b])

# # get is not gives error if there is not available
print("the meaning of your word is", a.get(b))
#print('my option are', a.keys[0])