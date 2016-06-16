import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
from bio_6 import probab_hidden_path as core

lines = readFile.listFromInput()
x = lines[0]
alphabet = lines[2]
path = lines[4]
states = lines[6]
headers, rows, matrix = core.parseTableFromLines(lines[8:])
print headers, rows, matrix
print x, alphabet, path, states
result = core.probabilityOfOutcomePath(x, path, headers, rows, matrix)
print result
readFile.lineToOutput(result)
    
