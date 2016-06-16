def overlapGraph(patterns):
	items = set(patterns)
	prefixes = {}
	for item in items:
		prefix = item[:-1]
		if (prefix in prefixes):
			prefixes[prefix].append(prefix)
		else:
			prefixes[prefix] = [item]
	results = []
	for item in items:
		suffix = item[1:]
		if suffix in prefixes:
			itemsWithPrefix = prefixes[suffix]
			def combineItemsLine(a,b):
				return "" + a + " -> " + b
			results = results + [combineItemsLine(item, x) for x in itemsWithPrefix]
	return results
