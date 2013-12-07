#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import networkx as nx

location = raw_input("Where are you? > ")
#dest = raw_input("where are you going >")

con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
	
with con:
	cur = con.cursor()
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + location + "'"
	cur.execute(sql)
	sID = cur.fetchone()
	print "System ID : %s " % sID
	
	#This will get all adjacent solar system IDs from the location
	rows = getRows(cur, location)
	for i in rows:
		print i[0]
   
	
	
def getRows (cur, location):
	sql = "select mapSolarSystemJumps.toSolarSystemID from mapSolarSystemJumps inner join " + \
	"mapSolarSystems on mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID " + \
	"where mapSolarSystems.solarSystemName ='" + location + "'"
	cur.execute(sql)
	rows = cur.fetchall()
	return rows
	
def checkMed (cur, station): #Returns true if a given station has cloning services returning true all the time right now
	return TRUE