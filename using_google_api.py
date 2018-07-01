import urllib.request,urllib.parse,urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = "federal institute of tecnology and education from southeastern Minas Gerais"
url = serviceurl + urllib.parse.urlencode({'address': address})
uh = urllib.request.urlopen(url)
data = uh.read().decode()

js = json.loads(data)

location = js['results'][0]['place_id']
print(location)
