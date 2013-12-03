

class route(object):
	def __init__(self, name, startPoint):
		self.name = name
		self.startPoint = startPoint
		self.jumps = {}
	
	def add_route(self, path):
		self.jumps.upate(path)
		
### What is the form I want this to be in? we have a start point, an end point and the number of jumps

def numJumps(start, end):
#Gets the start and end system and returns the number of jumps between them - get from api if possible
	jumps = 0
	return jumps

def systemName(system):
#makes sure the system name is valid, returns the name 
	name = system
	return name;