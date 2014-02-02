from nose.tools import *
import podJump.py

def test_router():
	router = pathFinder()
	assertIsNotNone(router.con)
	assertIsNotNone(router.map)
	assertEqual(router.map.number_of_nodes(), 7929)
	assertEqual(router.map.number_of_edges(), 7170) 

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
