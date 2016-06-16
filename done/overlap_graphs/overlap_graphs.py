import readFile

def run():
    listOfLines = readFile.listFromInput()
    prefixes, suffixes = prefixesAndSuffixes(listOfLines)
    result = zipPrefixesAndSuffixes(prefixes, suffixes)
    print result
    readFile.lineToOutput(result)

def prefixesAndSuffixes(lines):
    prefixes = {}
    suffixes = {}
    listPointer = 0
    node = ""
    recordSuffix = ""
    recordPrefix = ""
    while listPointer < len(lines):
        line = lines[listPointer]
        if line[0:1] == '>':
            addNote(prefixes, node, recordPrefix)
            addNote(suffixes, node, recordSuffix)
            node = line[1:]
            recordSuffix = ""
            recordPrefix = ""
        else:
            if recordPrefix == "":
                recordPrefix = line[:3]
            recordSuffix = line[-3:]
        listPointer += 1
    addNote(prefixes, node, recordPrefix)
    addNote(suffixes, node, recordSuffix)
    del prefixes[""]
    del suffixes[""]
    return (prefixes, suffixes)
    
def addNote(dict, data, key):
    if key in dict:
        list = dict[key]
        list.append(data)
    else:
        dict[key] = [ data ]

def zipPrefixesAndSuffixes(prefixes, suffixes):
    line = ""
    for prefixKey, prefixNodes in prefixes.items():
        for prefixNode in prefixNodes:
            if prefixKey in suffixes:
                suffixNodes = suffixes[prefixKey]
                for suffixNode in suffixNodes:
                    if suffixNode != prefixNode:
                        line += suffixNode + " " + prefixNode + '\n'
    return line.rstrip('\n')
        
    
