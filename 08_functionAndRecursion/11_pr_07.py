def remov_split(string, word):
    new_str= string.replace(word, "")
    return new_str.strip()

this = "avi is good"
s = remov_split(this, 'avi')
print(s)