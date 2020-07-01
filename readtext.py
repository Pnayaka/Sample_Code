fhand = open('mbox.txt')
count = 0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
