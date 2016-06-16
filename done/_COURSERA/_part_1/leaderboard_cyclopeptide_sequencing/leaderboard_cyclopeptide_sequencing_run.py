import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import leaderboardCyclopeptideSequencing as root

lines = readFile.listFromInput()
N = int(lines[0])
Spectrum = map(int, lines[1].split(" "))
LeaderBoard = root.leaderboardCyclopeptideSequencing(Spectrum, N)[0]
result = "-".join(map(str, LeaderBoard))
print result
readFile.lineToOutput(result)
    