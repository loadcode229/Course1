#largest word counter for a file.
#prompt for file name
fname = input('Enter file: ')

#if length of characters is less than 1, assume clown.txt.
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
#for handle, strip whitespace from line & print
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
#prints each word in wds seperately
    for w in wds:
#idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])

#print(di)

#now find the most common word *key/value
largest = -1
theword = None
for k,v in di.items():
    if v > largest :
        largest = v
        theword = k #capture/remember the key that was largest

print(theword,largest)
