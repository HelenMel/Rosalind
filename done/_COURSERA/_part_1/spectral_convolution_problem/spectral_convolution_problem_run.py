import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import spectralConvolutionProblem as root

lines = readFile.listFromInput()
Spectrum = map(int, lines[0].split(" "))
convolutionItems = root.convolution(Spectrum)
result = " ".join(map(str, convolutionItems))
print result
readFile.lineToOutput(result)
    
