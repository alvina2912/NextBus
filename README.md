
# NextBus
A simple utility application which will tell you how long it is until the next bus on “BUS ROUTE” leaving from “BUS STOP NAME” going “DIRECTION”
## Author
Alvina Pereira
## Prerequisites
[Python 2.7.11](https://www.python.org/downloads)
## Example
```
$ python NextBus.py 'METRO Green Line' 'Target Field Station Platform 1' 'EAST'
```

The above command will run NextBus and will tell you how long it is until the next bus

## About the app

1. The app uses [NexTrip API](http://svc.metrotransit.org/) to retrieve bus information.
2. The app uses ( http://svc.metrotransit.org/NexTrip/Routes) to retrieve routeID
3. The app uses ( http://svc.metrotransit.org/NexTrip/Directions/{ROUTE}) to retrieve directionValue
4. The app uses(http://svc.metrotransit.org/NexTrip/Stops/{ROUTE}/{DIRECTION}) to retrieve stopValue
5. The app uses ( http://svc.metrotransit.org/NexTrip/{ROUTE}/{DIRECTION}/{STOP}) to retrieve datetime value of the departure time.
6. Following is the list of available command line arguments. Arguments with * are mandatory arguments.
      * __busRoute*__ : A substring of the bus route name which is only in one bus route
      * __busStop*__ :A substring of the bus stop name which is only in one bus stop on that route
      * __direction*__ : can be “north” “east” “west” or “south”


##  Output

4 Minutes

## Running Test
```
$ python -m unittest discover Tests
```
