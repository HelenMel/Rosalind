import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import decoding_ideal_spectrum as core

lines = readFile.listFromInput()
result = core.decodingIdealSpectrum(lines[0])
print result
readFile.lineToOutput(result)
    
