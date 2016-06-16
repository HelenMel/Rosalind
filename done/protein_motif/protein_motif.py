import re
import readFile
import loadUniprotData

def run():
    ids = readFile.listFromInput()
    result = ""
    for uniprot_id in ids:
        protein = Protein(uniprot_id)
        result += protein.fetch_motif(motifPattern())
    result = result.rstrip('\n')
    print result
    readFile.lineToOutput(result)

def motifPattern():
    return re.compile('N[^P][ST][^P]')

class Protein():
    def __init__(self, uniprot_id):
        self._sequence = loadUniprotData.sequenceFromID(uniprot_id)
        self._uniprot_id = uniprot_id

    def _motif_iterator(self, motif_pattern):
        return motif_pattern.finditer(self._sequence)

    def _motif_search(self, motif_pattern, string):
        return motif_pattern.search(string)
    
    def _get_motif_indexes(self, motif_pattern):
        indexes = []
        search = self._motif_search(motif_pattern, self._sequence)
        index = 0
        sub = self._sequence
        while search:
            new_start = search.start() + 1
            index += search.start() + 1
            indexes.append(index)
            sub = sub[new_start:]
            search = self._motif_search(motif_pattern, sub)
        return indexes

    def fetch_motif(self, motif_pattern):
        indexes = self._get_motif_indexes(motif_pattern)
        if len(indexes) == 0:
            return ""
        answer = self._uniprot_id + '\n'
        for index in indexes:
            answer += str(index) + " "
        answer += '\n'
        return answer
        

        
        
