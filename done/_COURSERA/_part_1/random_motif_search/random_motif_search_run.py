import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import randomMotifSearch as root

lines = readFile.listFromInput()
k, t = map(int, lines[0].split(" "))
DNA = lines[1:]
result = "\n".join(root.repeatedRandomMotifSearch(DNA, k, t, 1000))
print result
readFile.lineToOutput(result)
    
