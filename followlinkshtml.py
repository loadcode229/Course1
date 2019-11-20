# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get input for url, open & read html, pare html and place in soup
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Get input for how many times to search
count = int(input('Enter count: '))

# Get input for which url to click on(-1 to make the position accurate)
position = int(input('Enter position: '))-1

while count >= 0:
    #re-reads current url
    html = urllib.request.urlopen(url, context=ctx).read()
    #creates new soup object
    soup = BeautifulSoup(html, 'html.parser')
    #searches the page for all <a> tags
    tags = soup('a')
    print("Retrieving: ", url)
    #updates the current url
    url = tags[position].get("href", None)
    count = count - 1
