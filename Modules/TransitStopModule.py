import json
import urllib
import Constants

stopUrl=Constants.BASE_URL+"Stops/{}/{}?format=json"

def getStopValue(routeID,DirectionValue,busStop):

    StopUrl=stopUrl.format(routeID,DirectionValue)
    uh = urllib.urlopen(StopUrl)
    data = uh.read()
    js = json.loads(str(data))
    item=0
    for item in range(len(js)):
        if js[item]['Text']!=busStop:
            continue
        else:
            stopValue= [item['Value'] for item in js if item['Text']==busStop][0]
            return stopValue
