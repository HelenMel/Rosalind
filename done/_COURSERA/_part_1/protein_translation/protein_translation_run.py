import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import proteinTranslation as root

Rna = readFile.lineFromInput()
result = root.rnaToProtein(Rna)
print result
readFile.lineToOutput(result)
    
