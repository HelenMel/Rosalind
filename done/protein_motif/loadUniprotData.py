import urllib2

database = "http://www.uniprot.org/uniprot/"

def sequenceFromID(uniprot_id):
    fasta_data = fastaFromID(uniprot_id)
    return fasta_data.sequence

def fastaFromID(uniprot_id):
    url = database + uniprot_id + ".fasta"
    response = urllib2.urlopen(url)
    return FASTA(response.read())
    
class FASTA:
    def __init__(self, data):
        lines = data.splitlines()
        self._name = lines[0][1:]
        fasta_sequence = ""
        for i in range(1, len(lines)):
            fasta_sequence += lines[i]
        self._sequence = fasta_sequence

    def get_name(self):
        return self._name

    name = property(get_name)

    def get_sequence(self):
        return self._sequence

    sequence = property(get_sequence)

    
