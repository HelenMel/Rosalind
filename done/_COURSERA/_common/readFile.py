def lineFromFile(fileName):
    f = open(fileName, 'r')
    line = f.read()
    line= line.rstrip('\n')
    f.close()
    return line;

def listFromFile(fileName):
    f = open(fileName, 'r')
    line = f.read()
    f.close()
    return line.splitlines()

def lineFromInput():
    return lineFromFile('input.txt')

def listFromInput():
    return listFromFile('input.txt')

def listFromOutput():
    return listFromFile('output_t.txt')

def lineToFile(fileName, line):
    f = open(fileName,'w')
    f.write(str(line))
    f.close()

def lineToOutput(line):
    fileOutput = 'output.txt'
    lineToFile(fileOutput, line)

def dictWithRNACodon():
    lines = listFromFile('rna_codon_table.txt')
    dict = {}
    for line in lines:
        sublines = line.split("   ")
        for subline in sublines:
            if subline == "":
                continue
            oneItem = subline.split(" ")
            dict[oneItem[0]] = oneItem[1]
    print len(dict)
    return dict

def FASTAline():
    FASTADict, length = FASTAdictFromInput()
    return FASTADict.values()[0]

def FASTAdictFromInput():
    listOfLines = listFromInput()
    listPointer = 0
    dict = {}
    recordName = ""
    recordData = ""
    while listPointer < len(listOfLines):
        line = listOfLines[listPointer]
        if line[0:1] == '>':
            dict[recordName] = recordData
            recordName = line[1:]
            recordData = ""
        else:
            recordData += line
        listPointer += 1
    dict[recordName] = recordData
    del dict[""]
    return dict, len(recordData)
        
    
