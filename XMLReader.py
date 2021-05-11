import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_944144.xml'
print(url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
   
stuff = ET.fromstring(str(soup))
comments = stuff.findall('comments/comment')
sum = 0
for x in comments:
    sum = sum + int(x.find('count').text)
    
print(sum)

