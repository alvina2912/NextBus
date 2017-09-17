import sys
import time
from Modules import RouteIDModule
from Modules import DirectionModule
from Modules import TransitStopModule
from Modules import TransitTimeModule

arguments = sys.argv

if arguments == None or len(arguments) < 4 :
    print "List of arguments has to be 3"
    sys.exit()
else:
    try:
        busRoute=arguments[1]
        busStop=arguments[2]
        direction=arguments[3]

        routeID = RouteIDModule.getRouteID(busRoute)

        if routeID == None:
            print "Bus Route "+ busRoute + " not found"
            sys.exit()

        directionValue=DirectionModule.getDirectionValue(routeID,direction)

        if directionValue == None:
            print "Bus Direction "+direction+" not found"
            sys.exit()
        stopValue=TransitStopModule.getStopValue(routeID,directionValue,busStop)

        if stopValue == None:
            print "Bus Stop "+busStop+" not found"
            sys.exit()

        timeValue = TransitTimeModule.getTime(routeID,directionValue,stopValue)
        if timeValue == None :
            print "Last bus for the day has already left"
            sys.exit()
        else:
            timeValue = timeValue[6:19]
            EpochTimeDifference = float(timeValue)-(float(time.time())*1000)
            MinuteTimeDifference = (EpochTimeDifference/(1000*60))
            print str(int(round(MinuteTimeDifference))) +' Minutes'
    except SystemExit:
        pass
    except:
        print "There was an error completing your request, please try again later"
