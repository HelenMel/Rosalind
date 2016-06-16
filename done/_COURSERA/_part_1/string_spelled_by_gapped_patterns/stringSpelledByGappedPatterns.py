import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import genomePath as gP

def parseGappedPatternsFromLines(lines):
	def lineToPattern(line):
		return line.split('|')
	return map(lineToPattern, lines)

# extend Node with second item
# construct graph
# glue together as graph

def stringSpelledByGappedPatterns(GappedPatterns, k, d):
	firstPatterns = [p[0] for p in GappedPatterns]
	secondPatterns = [p[1] for p in GappedPatterns]
	prefixString = stringSpelledByPatterns(firstPatterns, k)
	suffixString = stringSpelledByPatterns(secondPatterns, k)
	for x in xrange(k + d, len(prefixString)):
		if prefixString[x] != suffixString[x - k - d]:
			return "Error"
	return prefixString + suffixString[ -(k + d):]

	
def stringSpelledByPatterns(pattern, k):
	return gP.stringByGenomePath(pattern)