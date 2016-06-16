import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import readFile
import useful
import manhattanTourist as root

lines = readFile.listFromInput()
n, m = map(int, lines.pop(0).split(" "))
Down = []
line = lines.pop(0)
while line != "-":
    Down.append(map(int, line.split(" ")))
    line = lines.pop(0)
Right = []
line = lines.pop(0)
while True:
    Right.append(map(int, line.split(" ")))
    if len(lines) == 0:
        break;
    line = lines.pop(0)
root.extendDown(Down)
root.extendRight(Right)
result = root.ManhattanTourist(n, m, Down, Right)
print result
readFile.lineToOutput(result)
    
