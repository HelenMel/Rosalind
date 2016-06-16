import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import parse
import useful
import frequentWordsMismatches as FWM

lines = readFile.listFromInput()
Text = lines[0]
k, d =  map(int, lines[1].split(" "))
print Text, k, d
resultS = FWM.frequent_words_and_reverse_with_mismatches(Text, k, d)
result = useful.listStringToPrint(resultS)
print result
readFile.lineToOutput(result)
    