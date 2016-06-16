import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
from bio_3 import greedy_sorting as core

lines = readFile.listFromInput()
#line = "(+20 +7 +10 +9 +11 +13 +18 -8 -6 -14 +2 -4 -16 +15 +1 +17 +12 -5 +3 -19)"
perm = core.parsePermutation(lines[0])
steps = core.greedySorting(perm)
result = "\n".join([core.permutationToString(perm) for perm in steps[1:]])
print result
readFile.lineToOutput(result)
    
