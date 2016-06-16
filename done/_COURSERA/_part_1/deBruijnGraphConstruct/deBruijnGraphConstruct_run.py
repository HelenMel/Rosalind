import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import readFile
import parse
import useful
import deBruijnGraph

listOfLines = readFile.listFromInput()
result = useful.lineFromObjectsCollection(deBruijnGraph.deBruijnFromList(listOfLines))
print result
readFile.lineToOutput(result)
    
