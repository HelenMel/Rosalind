import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import parse
import useful
import overlapGraph

listOfLines = readFile.listFromInput()
print listOfLines
result = useful.lineFromCollection(overlapGraph.overlapGraph(listOfLines))
print result
readFile.lineToOutput(result)
    
