import readFile
import useful

def run():
    listOfLines = readFile.listFromInput()
    alphabet = listOfLines[0].split(" ")
    print "Start"
    length = int(listOfLines[1])
    repeat_count = pow(len(alphabet), length)
    f = open('output.txt','w')
    is_new = True
    for result in alphabetGenerator(repeat_count, alphabet, length):
        if is_new:
            is_new = False
        else:
            f.write('\n')
        f.write(result)
    f.close()
    print "Done"

# i ++
# for every generate numbers to current base
# convert numbers to string
# stop number? alphabet.count * length

def alphabetGenerator(n, alphabet, length):
    num = 0
    base = len(alphabet)
    while num < n:
        nums = convertToBase(num, base)
        nums = fitArrayToLength(nums, length)
        yield stringFromCharNumbers(nums, alphabet)
        num += 1

def convertToBase(num, base):
    nums = []
    i = 0
    reminder = 0
    rest = num
    while rest != 0 :
        reminder = rest % base
        rest = rest / base
        nums.append(reminder)
        i += 1
    return nums

def fitArrayToLength(char_numbers, length):
    diff = len(char_numbers) - length
    if diff == 0:
        return char_numbers
    else:
        if diff > 0:
            return char_numbers[:length]
        else:
            zeros = [0] * abs(diff)
            return char_numbers + zeros
    

def stringFromCharNumbers(char_numbers, alphabet):
    string = ""
    for char in char_numbers:
        string += alphabet[char]
    return string[::-1]


    
