
import useful
    
def parse(listOfLines):
	allData = listOfLines.split("--------\n")
	top = allData[0].rstrip('\n').split("\n")
	(k,m) = map(int, top[0].split(" "))
	def toPoint(string):
		return map(float, string.split(" "))
	Centers = map(toPoint, top[1:])

	bottom = allData[1].split("\n")
	print bottom
	Data = map(toPoint, bottom)
	return (k, m, Centers, Data)
