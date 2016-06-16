import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import out_LCS as root

sys.setrecursionlimit(10000)
lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
v = "AGACTG"
w = "GTACGA"
result = root.outputLCSRun(v, w)
print result
readFile.lineToOutput(result)
    
