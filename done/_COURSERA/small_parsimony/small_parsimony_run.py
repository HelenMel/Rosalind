import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import small_parsimony as core

lines = readFile.listFromInput()
n = int(lines[0])
Tree, Labels, m = core.parseStringsToTreeAndLabels(lines[1:])
totalCount, nodes = core.smallParsimony_run(Tree, Labels, m, n)
answer = [str(totalCount)] + nodes
result = "\n".join(answer)
print result
readFile.lineToOutput(result)
    
