import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import multiple_longest_sequence as mLS

sys.setrecursionlimit(10000)
lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
q = lines[2]
lines, score = mLS.outputLCSRun(v, w, q)
answer = [str(score), lines[0], lines[1], lines[2]]
result = "\n".join(answer)
print result
readFile.lineToOutput(result)
    
