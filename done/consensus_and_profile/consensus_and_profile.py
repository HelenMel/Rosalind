import readFile

def run():
    DNAStrings, DNALen = readFile.FASTAdictFromInput()
    print DNAStrings
    profile = { 'A': [], 'C': [], 'G': [], 'T': [] }
    consensus = ""
    for i in range(0, DNALen):
        bases = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
        for string in DNAStrings.values():
            bases = addOneToBase(string[i], bases)
        consensus += maxFromBases(bases)
        zipProfile(profile, bases)
    result = lineFromConsensusAndProfile(consensus, profile)
    print result
    readFile.lineToOutput(result)

def addOneToBase(char, bases):
    value = bases[char]
    bases[char] = value + 1
    return bases

    
def maxFromBases(bases):
    max = -1
    maxKey = ""
    for key, value in bases.items():
        if value > max:
            max = value
            maxKey = key
    return maxKey

def zipProfile(profile, bases):
    for key, value in profile.items():
        new_item = bases[key] 
        value.append(new_item)
        profile[key] = value

def lineFromConsensusAndProfile(consensus, profile):
    line = ""
    line += consensus + '\n'
    line += lineFromKey('A', profile['A'])
    line += lineFromKey('C', profile['C'])
    line += lineFromKey('G', profile['G'])
    line += lineFromKey('T', profile['T'])
    return line.rstrip('\n')

def lineFromKey(key, value):
    line = ""
    line += key + ":"
    for i in value:
        line += " " + str(i)
    line += '\n'
    return line
    
    
    
