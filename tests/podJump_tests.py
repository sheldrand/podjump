from nose.tools import *
import podJump.py

def test_router():
	router = pathFinder()
	assertIsNotNone(router.con)
	assertIsNotNone(router.map)
	assertEqual(router.map.number_of_nodes(), 5431)
	assertEqual(router.map.number_of_edges(), 5) #will currently fail, need to find the actual number of possible jumps

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
