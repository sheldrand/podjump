#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Ben'

import sqlite3 as lite
import sys
import networkx as nx

con = lite.connect('..\..\djangosite\sqlite-latest.db3')
new = lite.connect('routes.db3')

with con:
    cur = con.cursor()

    cur.execute("SELECT solarSystemID, solarSystemName FROM mapSolarSystems")
    map = nx.Graph()
    solarSystems = cur.fetchall()
    for system in solarSystems:
        map.add_node(system[0], name=system[1])
    cur.execute("SELECT fromSolarSystemID, toSolarSystemID FROM mapSolarSystemJumps")
    jumps = cur.fetchall()
    for i in jumps:
        map.add_edge(i[0], i[1])
        #		print map.number_of_edges()
        #		print map.number_of_nodes()
        # number of edges and number of nodes for testing
    data = nx.all_pairs_shortest_path(map, 1)
    #TODO figure out how to deal with the data coming in and put it in the database

    print data

print "if all else fails"
# new database layout: id, from system, to system, # jumps