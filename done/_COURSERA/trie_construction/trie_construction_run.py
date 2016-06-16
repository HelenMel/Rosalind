import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import trieConstruction as root
import trieGraph as tG

lines = readFile.listFromInput()
print lines
answer = root.trieNodesFromPatterns(lines)
result = "\n".join([ x.show() for x in answer])
print result
readFile.lineToOutput(result)
    
