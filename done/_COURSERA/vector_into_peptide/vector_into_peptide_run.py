import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
from bio_4 import peptide_into_vector as core

lines = readFile.listFromInput()
vectorPeptide = map(int, lines[0].split(" "))
print lines
result = core.vectorIntoPeptideRun(vectorPeptide)
print result
readFile.lineToOutput(result)
    
