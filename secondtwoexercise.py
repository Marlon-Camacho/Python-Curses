fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
nume = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = float(line[19:])
    count = count + 1.0

    nume = nume + num
    result = nume/count

print("Average spam confidence: "+str(result))
