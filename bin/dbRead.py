#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx

#Cloning serviceID is 512
class pathFinder(object):

	def __init__(self, server=['localhost', 'databaseHandler', 'test123', 'evedb']):
	#Innstantiates the pathFinder. Opens a connection to the database and builds the map.
		self.con = mdb.connect(server[0], server[1], server[2], server[3])
		self.cur = con.cursor()
		self.map = self.buildmap(self.cur)
		
	def podJump(self, dest, school, outerOffice):
	#Main function. Returns a list of offices sorted by distance from destination
	#List is of tuples (station, num jumps)
		offices = outerOffice #A local copy so as to not modify original list
		schools = schoolStations(self.cur, school)
		for i in schools:
			offices.append(i)
		clone = [] #Sorted list.
		for place in offices:
			if self.checkMed(cur, place):
				distance = shortestPath(cur, map, start, place)
				clone.append((place, distance))
			else:
				pass
		clone.sort(key=lambda tup: tup[1])
		return clone
		
	def getRows (self, cur, location):
	#depreciated, gets the systems around the location passed in
		sql = "SELECT mapSolarSystemJumps.toSolarSystemID FROM mapSolarSystemJumps INNER JOIN " + \
		"mapSolarSystems ON mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
		"WHERE mapSolarSystems.solarSystemName ='" + location + "'"
		cur.execute(sql)
		rows = cur.fetchall()
		return rows	

	def nameToID (self, name, cur=self.cur):
	#Takes in a system name and returns the system's ID number
		index = name.find(' ')#Only the first word (in case of funnyness)
		sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName LIKE '" + name[:index] + "%'"
		cur.execute(sql)
		sID = cur.fetchone()
		return sID
		
	def buildMap (self, cur):
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

	def shortestPath (self, cur, map, start, end):
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
			
	def checkMed (self, cur, station): 
	#Returns true if a given station has cloning services returning true all the time right now
		cur.execute("SELECT operationID FROM staOperationServices WHERE serviceID = '512'") 
		# gets a list of operationIDs with the cloning service
		operationList = cur.fetchall()
		sql = "SELECT operationID FROM staStations WHERE stationName LIKE '" + station + "%'"
		cur.execute(sql)
		stationType = cur.fetchone()
		if stationType in operationList:
			print "Station %r has cloning" % station
			return True
		else:
			return False	

	def readFile(self, fileName='stations'):
	#Reads a file for station names and parses them. Returns a lits of stations
	#	filename = raw_input("The name of your office file > ")
		corpOffices = open(fileName)
		line = corpOffices.readline()
		offices = []
		count = 0
		while line != '':
			index = line.rfind(' -')
			if index > 0:
				offices.append(line[:index])
			else:
				pass
			line = corpOffices.readline()
		print len(offices)
		return offices

	def schoolStations(self, cur, school):
	#returns a list of stations with cloning owned by that school.
	#Note: does not error check assumes school is picked from pre-populated list
		sql = "SELECT staStations.stationName FROM staStations INNER JOIN invNames ON staStations.corporationID=invNames.itemID " + \
		"WHERE invNames.itemName LIKE '" + school + "%';"

		cur.execute(sql)
		stations = cur.fetchall() #Gets the dump of all station names
		stationNames = []
		for pieces in stations: #Converts to a list of strings
			stationNames.append(pieces[0])
		return stationNames

if __name__ == "__main__":		
	con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb')
	with con:
		cur = con.cursor()
		map = buildMap(cur)
		

		start = raw_input("Where would you like to go? > ")
		school = raw_input("What school are you in > ")
		#end = raw_input("where are you going > ")
		
		
		sql = "SELECT solarSystemName from mapSolarSystems where solarSystemName LIKE '" + start + "%'"
		cur.execute(sql)
		n = cur.fetchone()
		print "Heading to %s" % n[0]
		
		
		
		offices = readFile()
		schools = schoolStations(cur, school) 
		for i in schools:
			offices.append(i)
		clone = [] #Sorted list.
		for place in offices:
			if checkMed(cur, place):
				distance = shortestPath(cur, map, start, place)
				clone.append((place, distance))
				print "and is %s Jumps from your destination \n" % distance
			else:
				pass
		clone.sort(key=lambda tup: tup[1])
		print clone
	print "end"
