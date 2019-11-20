from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter URL here, opens & reads the HTML, parses into soup.
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Find all span tags. Count & sum established
count = 0
tags = soup('span')
for tag in tags:
   # show contents(where comments & number of comments are)
   print('Contents:',tag.contents[0])
   # take the string number from contents
   strnum = tag.contents
   # turn strnum into a integer
   num = int(strnum[0-1])
   count = count + num
print(count)
