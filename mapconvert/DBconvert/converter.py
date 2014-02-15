#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Ben'

import sqlite3 as lite
import sys
import networkx as nx
import re

con = lite.connect('..\..\djangosite\sqlite-latest.db3')
new = lite.connect('routes.db3')

with con:
    cur = con.cursor()
    with new:
        build = new.cursor()

        cur.execute("SELECT solarSystemID, solarSystemName FROM mapSolarSystems")
        map = nx.Graph()
        solarSystems = cur.fetchall()
        for system in solarSystems:
            map.add_node(system[0], name=system[1])
        cur.execute("SELECT fromSolarSystemID, toSolarSystemID FROM mapSolarSystemJumps")
        gates = cur.fetchall()
        for i in gates:
            map.add_edge(i[0], i[1])
            #		print map.number_of_edges()
            #		print map.number_of_nodes()
            # number of edges and number of nodes for testing
        id = int(0)
        build.execute("DROP TABLE IF EXISTS routing_info")
        build.execute("CREATE TABLE routing_info(Id INT, from_system TEXT, to_system TEXT, num_jumps INT)")
        for source in solarSystems:
            print source[1]
            for dest in solarSystems:
                if nx.has_path(map, source[0], dest[0]):
                    jumps = len(nx.shortest_path(map, source[0], dest[0])) - 1
                    if jumps > 0:
                        id+=1
#                    print "INSERT INTO routing_info VALUES ({!s},{!s},{!s},{!s})".format(id, source, destination, jumps)
                        build.execute("INSERT INTO routing_info VALUES (?,?,?,?)", (id, source[1], dest[1], jumps))



#                    print "Going from %s to %s and is %s jumps" % (source[1], dest[1], jumps)



print "if all else fails"
# new database layout: id, from system, to system, # jumps