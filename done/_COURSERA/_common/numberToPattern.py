alphabet = ['A', 'C', 'G', 'T']

def numberToPattern(index,k):
	numbersIn4 = []
	while True:
		numbersIn4.append(index % 4)
		index = index / 4
		if index < 4:
			numbersIn4.append(index)
			break
	zeros = [0] * (k - len(numbersIn4))
	numbersIn4 = numbersIn4 + zeros
	def numberToLetter(n):
		return alphabet[n]
	numbersIn4.reverse()
	return ''.join(map(numberToLetter,numbersIn4))

def patternToNumber(Pattern):
	def letterToNumber(letter):
		return alphabet.index(letter)
	clumps = map(letterToNumber, list(Pattern))
	clumps.reverse()
	index = 0
	for i in xrange(0, len(clumps)):
		index += pow(4,i) * clumps[i]
	return index