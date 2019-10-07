#Use words.txt as the file name
fname = input("Enter file name: ")
fh = open('words.txt')
sum = fh.read()
up = sum.upper()
up = up.rstrip()
print(up)
