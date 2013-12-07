#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

location = raw_input("Where are you? > ")
#dest = raw_input("where are you going >")

con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
	
with con:
	cur = con.cursor()
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + location + "'"
	cur.execute(sql)
	sID = cur.fetchone()
	print "System ID : %s " % sID
	
	sql = "select mapSolarSystemJumps.toSolarSystemID from mapSolarSystemJumps inner join mapSolarSystems on mapSolarSystemJumps.fromSolarSystemID=mapSolarSystems.solarSystemID where mapSolarSystems.solarSystemName ='" + location + "'"
	cur.execute(sql)
	rows = cur.fetchall()
	for i in rows:
		print i[0]
   
	
	
# what I want to do is to select the name of all gates where the from is my location