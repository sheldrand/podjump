#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx


con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
map = nx.Graph()

def getRows (cur, location):
	sql = "select mapSolarSystemJumps.toSolarSystemID from mapSolarSystemJumps inner join " + \
	"mapSolarSystems on mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
	"where mapSolarSystems.solarSystemName ='" + location + "'"
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
	solarSystems = cur.fetchall()
	for system in solarSystems:
		map.add_node(system[0])
	cur.execute("SELECT fromSolarSystemID, toSolarSystemID FROM mapSolarSystemJumps")
	jumps = cur.fetchall()
	for i in jumps:
		map.add_edge(i[0], i[1])
	
with con:
	
	start = raw_input("Where are you? > ")
	end = raw_input("where are you going > ")
	
	cur = con.cursor()
	location = nameToID (cur, start)
	dest = nameToID (cur, end)
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + start + "'"
	cur.execute(sql)
	sID = cur.fetchone()
	print "System ID : %s " % sID
	
	#This will get all adjacent solar system IDs from the location
#	rows = getRows(cur, start)
#	for i in rows:
#		print i[0]
	
	buildMap(cur)
	
	path = nx.shortest_path(map, location[0], dest[0])
	distance = len(path)-1


   
	
	

	
def checkMed (cur, station): #Returns true if a given station has cloning services returning true all the time right now
	return TRUE