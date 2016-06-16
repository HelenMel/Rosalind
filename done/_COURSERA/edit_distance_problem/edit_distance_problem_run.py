import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import editDistanceProblem as eDP

sys.setrecursionlimit(10000)
lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
score = eDP.outputLCSRun(v, w)
result = str(-score)
print result

readFile.lineToOutput(result)
    
