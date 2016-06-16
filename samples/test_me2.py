fileName = 'rosalind_ini6.txt'

f = open(fileName, 'r')
input = f.read()
dict = {}
for word in input.split(' '):
    wordN = 0
    if word in dict:
        wordN = dict[word]
    wordN +=1
    dict[word] = wordN

for key, value in dict.items():
    print key + " " + str(value)
