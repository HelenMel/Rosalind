import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
from bio_6 import suffixArray as sA

lines = readFile.listFromInput()
Text = lines[0]
result = ", ".join(map(str, sA.suffixArray(Text)))
print result
readFile.lineToOutput(result)
    
