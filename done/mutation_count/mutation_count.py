import readFile

def run():
    listOfLines = readFile.listFromInput()
    mutations = 0
    strand1 = listOfLines[0]
    strand2 = listOfLines[1]
    for i in range(0, len(strand1)):
        if strand1[i] != strand2[i]:
            mutations += 1
    print mutations
