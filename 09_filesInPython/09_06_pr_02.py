def game():
    return  44
score = game()

with open("hiscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr=="":
    with open('hiscore.txt', 'w') as f:
         f.write(str(score))

elif int(hiscoreStr)<score:
    with open("hiscore.txt", 'w') as f:
        f.write(str(score))
else:
    pass
 