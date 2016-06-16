import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import DPChange as root

lines = readFile.listFromInput()
money = int(lines[0])
Coins = map(int, lines[1].split(","))
result = str(root.DPChange(money, Coins))
print result
readFile.lineToOutput(result)
    
