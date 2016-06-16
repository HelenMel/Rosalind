import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import useful
import medianString as root

lines = readFile.listFromInput()
k = int(lines[0])
Dna = lines[1:]
result = root.medianString(Dna, k)
print result
readFile.lineToOutput(result)
    
