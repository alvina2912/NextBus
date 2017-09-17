import json
import urllib
import Constants

directionUrl=Constants.BASE_URL+'Directions/{}?format=json'


def getDirectionValue(routeID,direction):
    DirectionUrl=directionUrl.format(routeID)
    uh = urllib.urlopen(DirectionUrl)
    data = uh.read()
    direction=direction.upper()
    diretionlist=['SOUTH','NORTH','EAST','WEST']

    js = json.loads(str(data))
    item=0

    for item in range(len(js)):
        if js[item]['Text']!=direction+'BOUND':
            continue
        else:
            diretionValue= [item['Value'] for item in js if item['Text']==direction+'BOUND'][0]
            return diretionValue
