import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import psm_search as core

lines = readFile.listFromInput()
SpectralVectors = []
for line in lines[:-2]:
    SpectralVectors.append(map(int, line.split(" ")))
Proteom = lines[-2]; threshold = lines[-1]
answer = core.PSMSearchRun(SpectralVectors, Proteom, threshold)
result = "\n".join(answer)
print result
readFile.lineToOutput(result)
    
