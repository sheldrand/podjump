#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx

#Cloning serviceID is 512

def getRows (cur, location):
#depreciated, gets the systems around the location passed in
	sql = "SELECT mapSolarSystemJumps.toSolarSystemID FROM mapSolarSystemJumps INNER JOIN " + \
	"mapSolarSystems ON mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
	"WHERE mapSolarSystems.solarSystemName ='" + location + "'"
	cur.execute(sql)
	rows = cur.fetchall()
	return rows	

def nameToID (cur, name):
#Takes in a system name and returns the system's ID number
	index = name.find(' ')#Only the first word (in case of funnyness)
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName LIKE '" + name[:index] + "%'"
	cur.execute(sql)
	sID = cur.fetchone()
	return sID
	
def buildMap (cur):
#Builds a networkx graph represting a map we will use for our calculations
	cur.execute("SELECT solarSystemID FROM mapSolarSystems")
	map = nx.Graph()
	solarSystems = cur.fetchall()
	for system in solarSystems:
		map.add_node(system[0])
	cur.execute("SELECT fromSolarSystemID, toSolarSystemID FROM mapSolarSystemJumps")
	jumps = cur.fetchall()
	for i in jumps:
		map.add_edge(i[0], i[1])
	return map

def shortestPath (cur, map, start, end):
#Takes a connection to a mySQL database containing the eve database, a map of the eve universe and 
#calculates the shortest path between the start and end systems given as strings

	beg = nameToID (cur, start)
	dest = nameToID (cur, end)
#	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + start + "'"
#	cur.execute(sql)
#	sID = cur.fetchone()
	path = nx.shortest_path(map, beg[0], dest[0])
	distance = len(path)-1
	return distance
		
def checkMed (cur, station): #Returns true if a given station has cloning services returning true all the time right now
	cur.execute("SELECT operationID FROM staOperationServices WHERE serviceID = '512'") # gets a list of operationIDs with the cloning service
	operationList = cur.fetchall()
	sql = "SELECT operationID FROM staStations WHERE stationName LIKE '" + station + "%'"
	cur.execute(sql)
	stationType = cur.fetchone()
	if stationType in operationList:
		print "Station %r has cloning" % station
		return True
	else:
		return False	

def readFile():
#Reads a file for station names and parses them. Returns a lits of stations
#	filename = raw_input("The name of your office file > ")
	corpOffices = open('sta')
	line = corpOffices.readline()
	offices = []
	count = 0
	while line != '':
		index = line.find(' -')
		if index > 0:
			offices.append(line[:index])
		else:
			pass
		line = corpOffices.readline()
	print len(offices)
	return offices


		
con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
with con:
	cur = con.cursor()
	map = buildMap(cur)

	start = raw_input("Where would you like to go? > ")
	#end = raw_input("where are you going > ")
	
	
	sql = "SELECT solarSystemName from mapSolarSystems where solarSystemName LIKE '" + start + "%'"
	cur.execute(sql)
	n = cur.fetchone()
	print "Heading to %s" % n[0]
	
	
	
	offices = readFile()
	clone = [] #This will be the sorted list how to sort it I'm not sure yet.
	for place in offices:
		if checkMed(cur, place):
			print "and is %s Jumps from your destination \n" % shortestPath(cur, map, start, place)
		else:
			pass
print "end"