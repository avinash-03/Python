with open('log.txt') as f:
    log=f.read()

if "python" in log.lower():
    print("yes there is present python")
else:
    prnt('there is no python')

