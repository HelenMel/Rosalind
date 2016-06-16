import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import readFile
import useful
import profileMostProbable as root

lines = readFile.listFromInput()
Text = lines[0]
k = int(lines[1])
Profile = []
for i in xrange(0,4):
	nucleotideProbabilities = map(float, lines[i + 2].split(" "))
	Profile.append(nucleotideProbabilities)
result = root.profileMostProbable(Text, k, Profile)
print result
readFile.lineToOutput(result)
    
