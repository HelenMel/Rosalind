import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import limbLength as lL

lines = readFile.listFromInput()
n = int(lines[0])
j = int(lines[1])
matrix = lines[2:]
S = []
[S.append(map(int, line.split(" "))) for line in matrix]
result = lL.limbLength(n, j, S)
print result
readFile.lineToOutput(result)
    
