import json
import urllib
import Constants

busRouteUrl=Constants.BASE_URL+'Routes?format=json'
def getRouteID(busRoute):
    uh = urllib.urlopen(busRouteUrl)
    data = uh.read()

    js = json.loads(str(data))
    
    item=0
    for item in range(len(js)):

        if js[item]['Description']!=busRoute:
            continue
        else:
            RouteID= [item['Route'] for item in js if item['Description']==busRoute][0]

            return RouteID
