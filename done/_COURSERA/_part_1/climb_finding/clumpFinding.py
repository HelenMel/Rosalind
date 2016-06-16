import frequentWords
import numberToPattern

def clumpFinding(Genome, k, t, L):
	FrequentPatterns = set()
	ClumpLen = (pow(4,k) - 1)
	Clump = [0] * ClumpLen
	for i in xrange(0, (len(Genome) - L)):
		Text = Genome[i:(i + L)]
		print "Text", Text
		FrequencyArray = frequentWords.frequencyArray(Text,k)
		print "FrequencyArray"
		print FrequencyArray
		for index in xrange(0, ClumpLen):
			if FrequencyArray(index) >= t:
				Clump[index] = 1
	for i in xrange(0,ClumpLen):
		if Clump(i) == 1:
			FrequentPatterns.add(numberToPattern.numberToPattern(i,k))
	return FrequentPatterns

def betterClumpFinding(Genome, k, t, L):
	#print 
	FrequentPatterns = set()
	ClumpLen = (pow(4,k) - 1)
	Clump = [0] * ClumpLen
	Text = Genome[0 : L]
	FrequencyArray = frequentWords.frequencyArray(Text,k)
	for i in xrange(0,ClumpLen):
		if FrequencyArray[i] >= t:
			#print "i is not zero", i
			Clump[i] = 1
	#print "LAst genome", len(Genome), len(Text)
	for i in xrange(1,(len(Genome) - L + 1)):
		#print "index", i
		FirstPattern = Genome[i - 1 : (i - 1) + k]
		#print "First Pattern", FirstPattern
		index = numberToPattern.patternToNumber(FirstPattern)
		#print "FrequencyArray START with index", FrequencyArray[index], index
		FrequencyArray[index] = FrequencyArray[index] - 1
		LastPattern = Genome[(i + L - k) : (i + L)]
		#print "Last pattern with index", LastPattern, (i + L - k)
		index = numberToPattern.patternToNumber(LastPattern)
		FrequencyArray[index] = FrequencyArray[index] + 1
		#print "FrequencyArray END with index", FrequencyArray[index], index
		if  FrequencyArray[index] >= t:
			#print "i is not zero", index
			Clump[index] = 1
	for i in xrange(0,ClumpLen):
		if Clump[i] == 1:
			Pattern = numberToPattern.numberToPattern(i, k)
			FrequentPatterns.add(Pattern)
	return FrequentPatterns
		
