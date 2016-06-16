import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import localAlignmentProblem as lAP

sys.setrecursionlimit(10000)
lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
lines, score = lAP.outputLCSRun(v, w)
answer = [str(score), lines[0], lines[1]]
result = "\n".join(answer)
print result
readFile.lineToOutput(result)
    
