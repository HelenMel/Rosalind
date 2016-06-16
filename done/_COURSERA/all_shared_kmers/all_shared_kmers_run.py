import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio3')))

import readFile
import useful
import all_shared_kmers as core

lines = readFile.listFromInput()
k = int(lines[0])
String1 = lines[1]
String2 = lines[2]
result = core.presentPairs(core.allSharedKMers(String1, String2, k))
print result
readFile.lineToOutput(result)
    
