#prompts user for file name
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

#reads file and establishes count
fh = open(fname)
count = 0

#searches for lines starting with 'From' and seperating them and counts them
for line in fh:
    line.rstrip()
    if line.startswith('From '):
        lines = line.split()
        print(lines[1])
        count += 1

#prints count of lines with From as the first word
print('There were', count, 'lines in the file with From as the first word')
