with open("poems.txt", "r") as f:
    a=f.read()
if 'twinkle' in a:
    print("twinkle is prestnt in the poem")
else:
    print('twinkle is not present')
