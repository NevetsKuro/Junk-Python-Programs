import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl, json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
url = 'http://py4e-data.dr-chuck.net/json?address=Belarusian%20State%20University&key=42'
parms['address'] = 'Belarusian State University'
parms['key'] = '42'
html = urllib.request.urlopen(url + urllib.parse.urlencode(parms) , context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
   
stuff = json.loads(str(soup))
#print(stuff)
sum = 0
placeID = stuff['results'][0]
print(placeID['place_id'])


