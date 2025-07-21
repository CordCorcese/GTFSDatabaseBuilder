import sqlite3

database = sqlite3.connect("TransitTracks.db")
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Stop (stopId Int PRIMARY KEY,stopName String,stopLat Double,stopLon Double,wheelchair Int,stopCode Int)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Route (routeID String PRIMARY KEY,routeShortName String,routeLongName String,routeType Int,routeColour String,routeTextColour String)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Trip (routeID String,serviceID Int,tripID String PRIMARY KEY,tripHeadSign String,shapeID Int,blockID Int,directionID Int)") 
cursor.execute("CREATE TABLE IF NOT EXISTS StopTime (tripID String,arrivalTime String,departureTime String,stopID Int,stopSequence Int,shapeDistTravelled Int,stopHeadSign Int,pickupType Int,dropOffType Int,timePoint INT, PRIMARY KEY (tripID, stopSequence))") 
cursor.execute("CREATE TABLE IF NOT EXISTS CalendarDate (serviceID Int,date String,exceptionType Int, PRIMARY KEY(serviceID, date))") 
cursor.execute("CREATE TABLE IF NOT EXISTS Shape (shapeID Int,shapePtLat Double,shapePtLon Double,shapePtSequence Int,shapeDistTravelled Int,PRIMARY KEY (shapeID, shapePtSequence))") 

stopTimeInsertSQL = '''INSERT INTO StopTime (tripID, arrivalTime, departureTime, stopID, stopSequence, shapeDistTravelled, stopHeadSign, pickupType, dropOffType, timepoint) VALUES (?,?,?,?,?,?,?,?,?,?)'''
stoptimes = open("stop_times.txt") 
stoptimes.readline().split(',') #skip info line
for row in stoptimes:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(stopTimeInsertSQL, splitline)
database.commit() 

stopInsertSQL = '''INSERT INTO Stop (stopId, stopName, stopLat, stopLon, wheelchair, stopCode) VALUES (?,?,?,?,?,?)'''
stops = open("stops.txt")
stops.readline()
for row in stops:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(stopInsertSQL, splitline)
database.commit()

routeInsertSQL = '''INSERT INTO Route (routeID, routeShortName, routeLongName, routeType, routeColour, routeTextColour) VALUES (?,?,?,?,?,?)'''
routes = open("routes.txt")
routes.readline()
for row in routes:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(routeInsertSQL,splitline)
database.commit()

tripsInsertSQL = '''INSERT INTO Trip (routeID, serviceID, tripID, tripHeadSign, shapeID, blockID, directionID) VALUES (?,?,?,?,?,?,?)'''
trips = open("trips.txt")
trips.readline()
for row in trips:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(tripsInsertSQL,splitline)
database.commit()

DateInsertSQL = '''INSERT INTO CalendarDate (serviceID, date, exceptionType) VALUES (?,?,?)'''
dates = open("calendar_dates.txt")
dates.readline()
for row in dates:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(DateInsertSQL,splitline)
database.commit()

shapeInsertSQL = '''INSERT INTO Shape (shapeID, shapePtLat, shapePtLon, shapePtSequence, shapeDistTravelled) VALUES (?,?,?,?,?)'''
shapes = open("shapes.txt")
shapes.readline()
for row in shapes:
    row.rstrip()
    splitline = row.split(',')
    cursor.execute(shapeInsertSQL,splitline)
database.commit()