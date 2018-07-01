import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_86331.json'
fhand = urllib.request.urlopen(url)

stringdemo = fhand.read().decode()

info = json.loads(stringdemo)
sum = 0
for i in info['comments']:
    sum += int(i['count'])
print(sum)
