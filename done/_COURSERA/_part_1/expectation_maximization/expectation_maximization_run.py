import sys, os
import numpy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_5')))

import readFile
import useful
import parse
import expectationMaximization as eM

lines = readFile.listFromInput()
k, m = map(int, lines[0].split(" "))
beta = float(lines[1])
Data = parse.parseToPoints(lines[2:])
#result = useful.listToPrint(eM.centersFromData(Data, beta, k, m, 100))
#print result
result = ""
Points = numpy.array([[2,8], [2,5], [6,9], [7,5], [5,2]])
Hidden = numpy.array([[0.5, 0.3, 0.8, 0.4, 0.9]])
some = eM.clusterToCenters(Points, Hidden, 5, 1, 2)
print "Some", some

Centers = numpy.array([[3,5], [5,4]])
some2 = eM.centersToClusters(Points, Centers, 1, 2, 2)
print "Some2", some2

readFile.lineToOutput(result)
    
