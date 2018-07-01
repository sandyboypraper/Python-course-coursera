import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_86330.xml'

fhand = urllib.request.urlopen(url)

strdemo = fhand.read()
tree = ET.fromstring(strdemo)

listreq = tree.findall('.//count')

sum = 0

for el in listreq:
    sum += int(el.text)
print(sum)


