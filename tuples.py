name = input("Enter file:")
handle = open(name)
hours = list()
count = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        line = line[5]
        line = line.split(':')
        line = int(line[0])
        hours.append(line)


hours.sort()

for hora in hours:
    if hora not in count:
        count[hora] = 1
    else:
        count[hora] = count[hora] + 1


for k,v in count.items():
    print('%02d'%k+' '+str(v))
        
