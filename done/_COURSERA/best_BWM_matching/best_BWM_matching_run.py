import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
from bio_6 import best_BWM_matching as bBM

lines = readFile.listFromInput()
Text = lines[0]
Patterns = lines[1:]
answer = bBM.bestBWMatchingRun(Text, Patterns)
result = " ".join(answer)
print result
readFile.lineToOutput(result)
    
