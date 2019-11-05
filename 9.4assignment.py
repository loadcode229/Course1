# Prompts for file name
name = input("Enter file: ")

#opens/reads file
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#makes empty list to be used later
lst = list()
#finds the word after 'from', counts, and adds it to list().
for line in handle:
    line = line.strip()
    if line.startswith("From: "):
        words = line.split()
        email = words[1]
        lst.append(email)
#makes dictionary and puts all emails from list() in dictionary and counts them.
dct = dict()
for email in lst:
    dct[email] = dct.get(email,0)+1

#declaring user who emailed most and largest number of times.
bigcount = None
bigem = None
for key, value in dct.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigem = key
#prints email that showed up the most and number of times.
print(bigem, bigcount)
