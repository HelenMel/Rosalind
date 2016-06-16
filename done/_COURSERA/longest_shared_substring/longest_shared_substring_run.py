import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import suffixTreeConstruction as sTC
import longestSharedSubstring as lSS

lines = readFile.listFromInput()
Text1 = lines[0]
Text2 = lines[1]
answer = lSS.longestSharedSubstring(Text1, Text2)
Text = lSS.combineString(Text1, Text2)
result = "".join([sTC.nodeStringFromText(x, Text) for x in answer])
print result
readFile.lineToOutput(result)
    
