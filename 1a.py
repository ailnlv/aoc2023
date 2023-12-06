with open('1.in', 'r') as f:
    lines = f.readlines()
    
sum = 0
for line in lines:
    first = 0
    last = 0
    for c in line:
        if '0' <= c <= '9':
            last = int(c)
            if first == 0:
                first = int(c)
    sum+=10*first+last

print(sum)
