def stringByGenomePath(path):
	string = path[0]
	for item in path:
		if item == string:
			continue
		string = string + item[-1:]
	return string