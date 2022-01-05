letter = '''Dear <|Name|>,
Greeting from ABC coding institute. You are selected for Executive
congratulation!
Have a great day ahead!
Thanks and regards
<|Date|>
'''
name = input("input your name\n")
date = input("enter date\n")
letter = letter.replace('<|Name|>',name)
letter = letter.replace('<|Date|>',date)
print(letter)