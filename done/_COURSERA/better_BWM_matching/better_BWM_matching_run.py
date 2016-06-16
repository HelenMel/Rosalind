import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import better_BWM_matching as bBm

lines = readFile.listFromInput()
LastColumn = lines[0]
Patterns = lines[1].split(" ")
answer = bBm.BWMatchingRun(LastColumn, Patterns)
result = " ".join(map(str, answer))
print result
readFile.lineToOutput(result)
    
