
with open('../pandas/errores-a-csv.txt', 'r') as f:
    data = f.read()

with open('/home/josejm/python-analysis/repositories.csv') as repos:
    datarepos = repos.read()

lines = data.splitlines()

print "begin"
num = 0
untilEnd = False
with open('remaining.txt', 'w') as frem:
    for line in lines:
        num += 1
        if line:
            if untilEnd:
                frem.write(line + '\n')
            elif not line in datarepos:
                untilEnd = True
                print num,
                print line
                frem.write(line + '\n')
        else:
            untilEnd = False
