
def composition(Text, k):
	end = len(Text) - k + 1
	items = []
	for x in xrange(0, end):
		items.append(Text[x : (x + k)])
	return items