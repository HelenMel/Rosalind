import math

def entropy(frequences):
	def probability(acc, f):
		if f == 0:
			return acc
		return acc + f * math.log(f,2)
	return -(reduce(probability, frequences, 0))

print entropy([0.25, 0, 0.5, 0.25])