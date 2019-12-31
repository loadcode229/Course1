import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#Specified URL is named
url = input('Enter - ')

#Opens & reads URL into 'data'
data = urllib.request.urlopen(url).read()
print('Retrieving: ', url)
print('Retrieved: ', len(data), 'characters')

#Parse all data from 'data' into 'tree'
tree = ET.fromstring(data)

#Find all 'count' elements & parse into 'counts'
counts = tree.findall('.//count')

#Extract the value of each count element and add it to the total
total_number = 0
sum = 0
for count in counts:
    sum += int(count.text)
    total_number += 1
print('Count:', total_number)
print('Sum: ', sum)
