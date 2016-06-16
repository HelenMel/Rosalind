import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import burrowWheelerTransform as bWT

lines = readFile.listFromInput()
Text = lines[0]
result = bWT.inverseBWT(Text)
print result
readFile.lineToOutput(result)
    
