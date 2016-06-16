def hamming_distance(string1, string2):
	dist = 0;
	for i in xrange(0, len(string1)):
		if string1[i] != string2[i]:
			dist += 1
	return dist

def hammingDistance(string1, string2):
	return hamming_distance(string1, string2)

def textToPatternsList(text, k):
	return [text[x: x+k] for x in xrange(0, (len(text) - k + 1))]