#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx

def getRows (cur, location):
	sql = "SELECT mapSolarSystemJumps.toSolarSystemID FROM mapSolarSystemJumps INNER JOIN " + \
	"mapSolarSystems ON mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
	"WHERE mapSolarSystems.solarSystemName ='" + location + "'"
	cur.execute(sql)
	rows = cur.fetchall()
	return rows	

def nameToID (cur, name):
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName LIKE '" + name + "%'"
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

def shortestPath (con, map, start, end):
		
	with con:
		cur = con.cursor()
		beg = nameToID (cur, start)
		dest = nameToID (cur, end)
		sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + start + "'"
		cur.execute(sql)
		sID = cur.fetchone()
		path = nx.shortest_path(map, beg[0], dest[0])
		distance = len(path)-1
		return distance
		
def checkMed (cur, station): #Returns true if a given station has cloning services returning true all the time right now
	return TRUE	

def readFile():
	filename = raw_input("The name of your office file > ")
	corpOffices = open('sta')
	line = corpOffices.readline()
	offices = []
	while line != '':
		index = line.find(' ')
		offices.append(line[:index])
		line = corpOffices.readline()
	print len(offices)
	return offices



		
con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
with con:
	c = con.cursor()
	map = buildMap(c)

start = raw_input("Where are you? > ")
#end = raw_input("where are you going > ")

offices = readFile()
i = 1
for place in offices:
	print "there have been %r" % i
	i += 1
	print shortestPath(con, map, start, place)
print shortestPath(con, map, start, end)
print "end"