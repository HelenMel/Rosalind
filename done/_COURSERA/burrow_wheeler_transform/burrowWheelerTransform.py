def inverseBWT(Text):
    #numerate last row
    lastNumerated = textToNumerated(Text)
    firstString = sorted(Text)
    firstNumerated = textToNumerated(firstString)
    BWT = ""
    current = '$1'
    for i in xrange(0, len(Text)):
        opponentIndex = lastNumerated.index(current)
        opponent = firstNumerated[opponentIndex]
        BWT += opponent[0]
        current = opponent
    return BWT

def textToNumerated(Text):
    numerated = []
    counts = {}
    for i in xrange(0, len(Text)):
        letter = Text[i]
        place = 1
        if letter in counts:
            place = counts[letter]
        newLetterName = letter + str(place)
        place += 1
        counts[letter] = place
        numerated.append(newLetterName)
    return numerated

#print inverseBWT("ard$rcaaaabb")