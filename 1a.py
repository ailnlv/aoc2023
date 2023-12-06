with open('1.in', 'r') as f:
    lines = f.readlines()

numbers = dict(
    one=1,
    two=2,
    three=3,
    four=4,
    five=5,
    six=6,
    seven=7,
    eight=8,
    nine=9,
)

sum = 0

for line in lines:
    first = 0
    last = 0
    for i, c in enumerate(line):
        if '1' <= c <= '9':
            last = int(c)
            if first == 0:
                first = int(c)
            continue
        for k, v in numbers.items():
            subword = line[i:i + len(k)]
            if subword == k:
                last = v
                if first == 0:
                    first = v
                break
    sum+=10*first+last

print(sum)
