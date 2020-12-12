handle = open("mbox-short.txt")

emails = dict()
email = list()

for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        lines = line.split(' ')
        email.append(lines[1])

for e in email:
    if e not in emails:
        emails[e] = 1
    else :
        emails[e] = emails[e] + 1

maxc = None
maxw = None
for e,c in emails.items():
    if maxc is None or c > maxc:
        maxw = e
        maxc = c

print(maxw, maxc)
