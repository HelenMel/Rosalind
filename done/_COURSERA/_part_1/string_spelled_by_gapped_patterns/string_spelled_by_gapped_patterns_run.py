import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import parse
import useful
import stringSpelledByGappedPatterns as sBGP

lines = readFile.listFromInput()
k, d = map(int, lines[0].split(" "))
print k, d
patterns = sBGP.parseGappedPatternsFromLines(lines[1:])
result = sBGP.stringSpelledByGappedPatterns(patterns, k, d)
print result
readFile.lineToOutput(result)
    
