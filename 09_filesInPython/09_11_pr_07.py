content = True
i=1

with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():

                 print(content)
                 print(f'***the python present in the line no {i}****')
        i+=1
