import sys

def minimum_skew(Genome):
	s = 0
	minSkew = sys.maxint
	minSkewIndexes = []
	for i in xrange(0, len(Genome)):
	    s = skew(i, Genome, s)
	    if s < minSkew:
	    	minSkew = s
	    	minSkewIndexes = [i + 1]
	    elif s == minSkew:
	    	minSkewIndexes.append(i + 1)
	return [str(x) for x in minSkewIndexes]

def skew(index, Genome, s):
	if Genome[index] == 'G':
		s += 1
	elif Genome[index] == 'C':
		s -= 1 
	return s