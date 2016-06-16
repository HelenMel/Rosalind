import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import suffixTreeConstruction as sTC

lines = readFile.listFromInput()
Text = lines[0]
answer = sTC.modifiedSuffixTreeConstruction(Text)
answer = [sTC.nodeStringFromText(x, Text) for x in answer]
result = "\n".join(answer)
print result
print "done"
readFile.lineToOutput(result)
    
