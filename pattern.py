line = '*'
max_length =10

while len(line)<=max_length:
    print(line)
    line +="*"
    
    while len(line)>0:
        print(line)
        line=line[:-1]