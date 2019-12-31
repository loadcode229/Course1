import urllib.request as ur
import json

#Enter URL
url = input("Enter - ")
#Retrieving specified URL
print("Retrieving: ", url)
#Open, Read, Pull all data and Decode from UTF to Unicode into data.
data = ur.urlopen(url).read().decode()
#Retrieved number of characters.
print("Retrieved: ", len(data), 'characters')
#Parses json data into "obj"
obj = json.loads(data)

#sum & total_number specified
sum = 0
total_number = 0

#For comment in all of the "comments" in obj data
for comment in obj["comments"]:
    #Add the integers from //"count" into "sum"
    sum += int(comment["count"])
    #Count total number of different "count"
    total_number += 1

print("Count: ", total_number)
print('Sum: ', sum)
