import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import trieConstruction as tC
import trieMatching as tM

lines = readFile.listFromInput()
Text = lines[0]
Patterns = lines[1:]
Trie, root = tC.trieNodesAndRootFromPatterns(Patterns)
answer = tM.trieMatching(Text, Trie, root)
result = " ".join(map(str,answer))
print result
readFile.lineToOutput(result)
    
