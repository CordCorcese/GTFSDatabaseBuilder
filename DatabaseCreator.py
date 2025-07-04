import sqlite3

database = sqlite3.connect("TransitTracks.db")
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Stop (stopId Int PRIMARY KEY,stopName String,stopLat Double,stopLon Double,wheelchair Int,stopCode Int)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Route (routeID String PRIMARY KEY,routeShortName String,routeLongName String,routeType Int,routeColour String,routeTextColour String)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Trip (routeID String,serviceID Int,tripID String PRIMARY KEY,tripHeadSign String,shapeID Int,blockID Int,directionID Int)") 
cursor.execute("CREATE TABLE IF NOT EXISTS StopTime (tripID String,arrivalTime String,departureTime String,stopID Int,stopSequence Int,shapeDistTravelled Int,stopHeadSign Int,pickupType Int,dropOffType Int,PRIMARY KEY (tripID, stopSequence))") 
cursor.execute("CREATE TABLE IF NOT EXISTS CalendarDate (serviceID Int,date String PRIMARY KEY,exceptionType Int)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Shape (shapeID Int,shapePtLat Double,shapePtLon Double,tripHeadSign String,shapePtSequence Int,shapeDistTravelled Int,PRIMARY KEY (shapeID, shapePtSequence))") 

stoptimes = open("stop_times.txt") 
stoptimes.readline().split(',') #skip info line

stopTimeInsertSQL = '''INSERT INTO StopTime (tripID, arrivalTime, departureTime, stopID, stopSequence, shapeDistTravelled, stopHeadSign, pickupType, dropOffType) VALUES (?,?,?,?,?,?,?,?,?)'''
for row in stoptimes:
    splitline = row.split(',')
    for x in splitline:
        x.strip()
        print(x)
    

stopInsertSQL = '''INSERT INTO Stop (stopId, stopName, stopLat, stopLon, wheelchair, stopCode) VALUES (?,?,?,?,?,?)'''
stops = open("stops.txt")

routeInsertSQL = '''INSERT INTO Route (routeID, routeShortName, routeLongName, routeType, routeColour, routeTextColour) VALUES (?,?,?,?,?,?)'''
routes = open("routes.txt")

tripsInsertSQL = '''INSERT INTO Trip (routeID, serviceID, tripID, tripHeadSign, shapeID, blockID, directionID) VALUES (?,?,?,?,?,?,?)'''
trips = open("trips.txt")

DateInsertSQL = '''INSERT INTO CalendarDate (serviceID, date, exceptionType) VALUES (?,?,?)'''

shpaeInsertSQL = '''INSERT INTO Shape (shapeID, shapePtLat, shapePtLon, tripHeadSign, shapePtSequence, shapeDistTravelled) VALUES (?,?,?,?,?,?)'''