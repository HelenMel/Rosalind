def parseTableFromLines(lines):
    letters = lines[0].split("\t")
    if letters[0] == "":
        letters = letters[1:]
    headers = dict(zip(letters, xrange(0, len(letters))))
    rows = {}
    matrix = []
    i = 0
    for row in lines[1:]:
        values = row.split("\t")
        if values[-1] == "":
            values = values[:-1]
        rows[values.pop(0)] = i; i+=1
        values = map(float, values)
        matrix.append(values)
    return headers, rows, matrix

def probabilityOfHiddenPath(path, headers, rows, matrix):
    total = 0.5
    for i in xrange(0, len(path) - 1):
        startSymbol = path[i]; endSymbol = path[i + 1]
        prob = matrix[rows[startSymbol]][headers[endSymbol]]
        total *= prob
    return total

def probabilityOfOutcomePath(x, path, headers, rows, matrix):
    total = 1
    for i in xrange(0, len(x)):
        emittedSymbol = x[i]; state = path[i]
        prob = matrix[rows[state]][headers[emittedSymbol]]
        total *= prob
    return total


