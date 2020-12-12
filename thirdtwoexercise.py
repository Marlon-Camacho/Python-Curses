fh = open("mbox-short.txt")
count = 0

for line in fh:
    if line.startswith('From '):
        count = count + 1
        print(line.split(' ')[1])


print("There were "+str(count)+" lines in the file with From as the first word")
