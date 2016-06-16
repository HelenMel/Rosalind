import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import peptideEncoding as root

lines = readFile.listFromInput()
Dna = "".join(lines)
Peptide = "VKLFPWFNQY"
print Dna, Peptide
result = useful.lineFromCollection(root.peptideEncoding(Dna, Peptide))
print result
readFile.lineToOutput(result)
    
