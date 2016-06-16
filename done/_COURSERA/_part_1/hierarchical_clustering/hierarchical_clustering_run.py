import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_5')))

import readFile
import useful
import hierarchicalClustering as hC

lines = readFile.listFromInput()
n = int(lines[0])
D = [[float(x) for x in line.split(" ")] for line in lines[1:]]
result = useful.lineFromCollection(hC.hierarchicalClustering(D, n))
print result
readFile.lineToOutput(result)
    
