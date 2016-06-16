
import useful
    
def parse(listOfLines):
	(k,m) = map(int, listOfLines[0].split(" "))
	def toPoint(string):
		return map(float, string.split(" "))
	Data = map(toPoint, listOfLines[1:])
	return (Data, k, m)

def parseToPoints(lines):
	def toPoint(string):
		return map(float, string.split(" "))
	Data = map(toPoint, lines)
	return Data