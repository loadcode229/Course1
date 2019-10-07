# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
average = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(" ")
    value = line[pos:]
    value = float(value)
    count = count + 1
    average = average + value

print("Average spam confidence:", average/count)
