import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import suffixTreeConstruction as sTC
import shortesNonSharedSubstring as sNSS
import dirtyHack as dH

lines = readFile.listFromInput()
Text1 = lines[0]
Text2 = lines[1]
result = dH.compareTwo(Text1, Text2)
#answer = sNSS.shortestNonSharedSubstring(Text1, Text2)
#Text = sNSS.combineString(Text1, Text2)
#print answer
#result = "".join([sTC.nodeStringFromText(x, Text) for x in answer])
print result
readFile.lineToOutput(result)
    
