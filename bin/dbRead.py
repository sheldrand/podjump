#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

location = raw_input("Where are you? > ")

con = mdb.connect('localhost', 'databaseHandler', 'test123', 'evedb');
	
with con:
	cur = con.cursor()
	sql = "SELECT solarSystemID from mapSolarSystems where solarSystemName = '" + location + "'"
	cur.execute(sql)
	sID = cur.fetchone()
   
	print "System ID : %s " % sID    