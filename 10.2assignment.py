#prompts user for file name and reads it
name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
#makes empty dictionary called hours
hours = dict()
#strip lines in fh, search for "From ", split into words.
for line in fh:
    line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
#search for the time in hour and seperate from ":"
    hour = words[5].split(":")
#counts all hours up and stores in hours.
    hours[hour[0]] = hours.get(hour[0],0) + 1
#empty list
lst = []
#for a,b items in hours, add to the list.
for a,b in hours.items():
    lst.append((a,b))
#sorts list
lst.sort()
#print a,b in the list.
for a,b in lst:
    print(a,b)
