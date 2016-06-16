import readFile

    
def run():
    listOfLines = readFile.listFromInput()
    maxRecord = recordsDictFromList(listOfLines)
    print "" + maxRecord.name + " \n" + str(maxRecord.data * 100)

def recordsDictFromList(listOfLines):
    listPointer = 0
    record = Record("")
    maxRecord = record
    while listPointer < len(listOfLines):
        line = listOfLines[listPointer]
        if line[0:1] == '>':
            if record.data > maxRecord.data:
                maxRecord = record
            recordName = line[1:]
            record = Record(recordName)
        else:
            record.add_line(line)
        listPointer += 1
    if record.data > maxRecord.data:
        maxRecord = record
    return maxRecord

class Record:
    def __init__(self, name):
        self._name = name
        self._totalLength = 0
        self._CGLength = 0

    def get_name(self):
        return self._name
    name = property(get_name)

    def add_line(self, line):
        self._totalLength += len(line)
        cgLine = line.translate(None, 'A,T')
        self._CGLength += len(cgLine)

    def get_data(self):
        if self._totalLength == 0:
            return 0;
        return float(self._CGLength) / float(self._totalLength)
    data = property(get_data)
            
             
            
