import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
from bio_6 import probab_hidden_path as core

lines = readFile.listFromInput()
path = lines[0]
States = lines[2].split(" ")
headers, rows, matrix = core.parseTableFromLines(lines[4:])
print headers, rows, matrix
result = core.probabilityOfHiddenPath(path, headers, rows, matrix)
print result
readFile.lineToOutput(result)
    
