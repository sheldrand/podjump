#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx

#Cloning serviceID is 512
class pathFinder(object):

	def __buildMap (self, cur):
	#Builds a networkx graph represting a map we will use for our calculations
		self.cur.execute("SELECT solarSystemID FROM mapSolarSystems")
		map = nx.Graph()
		solarSystems = cur.fetchall()
		for system in solarSystems:
			map.add_node(system[0])
		cur.execute("SELECT fromSolarSystemID, toSolarSystemID FROM mapSolarSystemJumps")
		jumps = cur.fetchall()
		for i in jumps:
			map.add_edge(i[0], i[1])
#		print number of edges and number of nodes for testing
		return map
		
	def __init__(self, server=['localhost', 'databaseHandler', 'test123', 'evedb']):
	#Innstantiates the pathFinder. Opens a connection to the database and builds the map.
		self.con = mdb.connect(server[0], server[1], server[2], server[3])
		self.cur = self.con.cursor()
		self.map = self.__buildMap(self.cur)
		
	def podJump(self, dest, school, outerOffice):
	#Main function. Returns a list of offices sorted by distance from destination
	#List is of tuples (station, num jumps)
	#Input: destination, a string representing a school and a list of offices (usually generated from readFile
		offices = outerOffice #A local copy so as to not modify original list
		schools = self.schoolStations(self.cur, school) # Gets the school stations from the school string
		for i in schools:
			offices.append(i) #Add schools to the offices list
		clone = [] #Sorted list.
		for place in offices:
			if self.checkMed(self.cur, place):
				distance = self.shortestPath(self.cur, self.map, dest, place)
				clone.append((place, distance))
			else:
				pass
		clone.sort(key=lambda tup: tup[1])
		return clone
	
	def __enter__(self):
		return pathFinder() #creating a new copy of the class
	
	def __exit__(self, type, value, traceback):
		self.con.close() #closing my cursor object
	pass
	
	def getRows (self, cur, location):
	#depreciated, gets the systems around the location passed in
		sql = "SELECT mapSolarSystemJumps.toSolarSystemID FROM mapSolarSystemJumps INNER JOIN " + \
		"mapSolarSystems ON mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
		"WHERE mapSolarSystems.solarSystemName ='" + location + "'"
		self.cur.execute(sql)
		rows = cur.fetchall()
		return rows	

	def nameToID (self, cur, name):
	#Takes in a system name and returns the system's ID number
		index = name.find(' ')#Only the first word (in case of funnyness)
		sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName LIKE '" + name[:index] + "%'"
		self.cur.execute(sql)
		sID = self.cur.fetchone()
		return sID
		


	def shortestPath (self, cur, map, start='jita', end='vfk'):
	#Takes a connection to a mySQL database containing the eve database, a map of the eve universe and 
	#calculates the shortest path between the start and end systems given as strings
		beg = self.nameToID (self.cur, start)
		dest = self.nameToID (self.cur, end)
		path = nx.shortest_path(self.map, beg[0], dest[0])
		distance = len(path)-1
		return distance
			
	def checkMed (self, cur, station): 
	#Returns true if a given station has cloning services returning true all the time right now
		self.cur.execute("SELECT operationID FROM staOperationServices WHERE serviceID = '512'") 
		# gets a list of operationIDs with the cloning service
		operationList = self.cur.fetchall()
		sql = "SELECT operationID FROM staStations WHERE stationName LIKE '" + station + "%'"
		self.cur.execute(sql)
		stationType = self.cur.fetchone()
		if stationType in operationList:
			return True
		else:
			return False	

	def readFile(self, fileName='stations'):
	#Reads a file for station names and parses them. Returns a lits of stations
		corpOffices = open(fileName)
		line = corpOffices.readline()
		offices = []
		while line != '':
			index = line.rfind(' -')
			if index > 0:
				offices.append(line[:index])
			else:
				pass
			line = corpOffices.readline()
		return offices

	def schoolStations(self, cur, school='science and trade'):
	#returns a list of stations with cloning owned by that school.
	#Note: does not error check assumes school is picked from pre-populated list
		sql = "SELECT staStations.stationName FROM staStations INNER JOIN invNames ON " + \
		"staStations.corporationID=invNames.itemID WHERE invNames.itemName LIKE '" + school + "%';"

		self.cur.execute(sql)
		stations = self.cur.fetchall() #Gets the dump of all station names
		stationNames = []
		for pieces in stations: #Converts to a list of strings
			stationNames.append(pieces[0])
		return stationNames

if __name__ == "__main__":
	#this probably doesn't work right now.
	
	path = pathFinder()
	start = raw_input("Where would you like to go? > ")
	school = raw_input("What school are you in > ")
	
	offices = path.readFile()
	sorted = path.podJump(start, school, offices)
	con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb')
	with con:
		cur = con.cursor()
		sql = "SELECT solarSystemName from mapSolarSystems where solarSystemName LIKE '" + start + "%'"
		cur.execute(sql)
		n = cur.fetchone()
	
	print "Heading to %s \n\n" % n[0]	
	for i in sorted:
		print "Office at %s is %s jumps from destination \n" % (i[0],i[1])
#		map = __buildMap(cur)
	print "end"
