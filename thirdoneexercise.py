fh = open('romeo.txt')
lst = []
for line in fh:
    med = line.split()
    for element in med:
        if element not in lst:
            lst.append(element)

lst.sort()
print(lst[:])  
