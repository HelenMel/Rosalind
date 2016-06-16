import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import multiple_approx_matching as mAM

lines = readFile.listFromInput()
Text = lines[0]
Patterns = lines[1].split(" ")
d = int(lines[2])
answer = mAM.multipleApproximatePatternsMatching(Text, Patterns, d)
result = " ".join(answer)
print result
readFile.lineToOutput(result)
    
