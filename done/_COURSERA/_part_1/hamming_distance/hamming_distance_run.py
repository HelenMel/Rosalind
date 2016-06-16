import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import parse
import useful
import hammingDistance

lines = readFile.listFromInput()
print lines
line1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
line2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
result = hammingDistance.hamming_distance(line1, line2)
print result
readFile.lineToOutput(result)
    
