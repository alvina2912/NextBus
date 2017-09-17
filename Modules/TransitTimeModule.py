import json
import urllib
import Constants

timeUrl=Constants.BASE_URL+'{}/{}/{}?format=json'

def getTime(routeID,DirectionValue,StopValue):
    TimeUrl=timeUrl.format(routeID,DirectionValue,StopValue)
    uh = urllib.urlopen(TimeUrl)
    data = uh.read()
    js = json.loads(str(data))
    if len(js) == 0 :
        return None
    else:
        timeValue=js[0]['DepartureTime']
        return timeValue
