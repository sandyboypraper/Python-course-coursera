from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Roslin.html'
count = input()
position = input()
name = ""

for i in range(0, int(count)):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag = tags[int(position)-1]
    url = tag.get('href', None)
    names = url.split('_')
    yo = reversed(names)
    namel = list(yo)[0].split('.')
    name = namel[0]
print(name)


