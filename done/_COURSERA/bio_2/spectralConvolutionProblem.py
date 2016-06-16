def convolution(Spectrum):
	ConvolutionItems = []
	s = sorted(Spectrum)
	for i in xrange(0, len(s)):
		for j in xrange(0, i):
			item = s[i] - s[j]
			if item > 0:
				ConvolutionItems.append(item)
	return ConvolutionItems