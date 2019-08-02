import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Retrieve all of the anchor tags

url = input('Enter - ')
count=input('Enter count: ')
count=int(count)
pos=input('Enter pos :')
pos=int(pos)
r=0
while r<count :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    prog=1
    for tag in tags:
        #print(tag.get('href', None))
        url=tag.get('href', None)
        if prog==pos : break
        #print(prog)
        prog = prog + 1
    print('Retrieveing: ', url)
    r=r+1
