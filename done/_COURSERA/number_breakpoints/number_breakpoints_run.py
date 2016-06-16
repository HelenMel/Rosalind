import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
from bio_3 import greedy_sorting as core

lines = readFile.listFromInput()
perm = core.parsePermutation(lines[0])
print perm
result = core.numberOfBreakpoints(perm)
print result
readFile.lineToOutput(result)
    
