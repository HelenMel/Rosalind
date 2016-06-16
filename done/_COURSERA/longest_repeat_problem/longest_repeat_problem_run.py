import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import suffixTreeConstruction as sTC
import longestRepeatProblem as lRP

lines = readFile.listFromInput()
Text = lines[0] + "$"
#Text = "panamabananas$"
Tree, root = sTC.modifiedSuffixTreeConstructionWithRoot(Text)
answer = lRP.longestRepeatProblem(Tree, root)
result = "".join([sTC.nodeStringFromText(x, Text) for x in answer])
print result
readFile.lineToOutput(result)
    
