import sqlite3

database = sqlite3.connect("TransitTracks.db")
cursor = database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Stop (stopId INTEGER PRIMARY KEY NOT NULL,stopName TEXT,stopLat REAL NOT NULL,stopLon REAL NOT NULL,wheelchair INTEGER NOT NULL,stopCode INTEGER NOT NULL)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Route (routeID TEXT PRIMARY KEY NOT NULL,routeShortName TEXT NOT NULL,routeLongName TEXT NOT NULL,routeType INTEGER NOT NULL,routeColour TEXT NOT NULL,routeTextColour TEXT NOT NULL)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Trip (routeID TEXT NOT NULL,serviceID INTEGER NOT NULL,tripID TEXT PRIMARY KEY NOT NULL,tripHeadSign TEXT NOT NULL,shapeID INTEGER NOT NULL,blockID INTEGER NOT NULL,directionID INTEGER NOT NULL)") 
cursor.execute("CREATE TABLE IF NOT EXISTS StopTime (tripID TEXT NOT NULL,arrivalTime TEXT NOT NULL,departureTime TEXT NOT NULL,stopID INTEGER NOT NULL,stopSequence INTEGER NOT NULL,shapeDistTravelled INTEGER NOT NULL,stopHeadSign TEXT,pickupType INTEGER NOT NULL,dropOffType INTEGER NOT NULL,timePoint INTEGER NOT NULL, PRIMARY KEY (tripID, stopSequence))") 
cursor.execute("CREATE TABLE IF NOT EXISTS CalendarDate (serviceID INTEGER NOT NULL,date TEXT NOT NULL PRIMARY KEY,exceptionType INTEGER NOT NULL)") 
cursor.execute("CREATE TABLE IF NOT EXISTS Shape (shapeID INTEGER NOT NULL,shapePtLat REAL NOT NULL,shapePtLon REAL NOT NULL,shapePtSequence INTEGER NOT NULL,shapeDistTravelled INTEGER NOT NULL,PRIMARY KEY (shapeID, shapePtSequence))") 

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