import sys
import readFile

def run():
    dictOfStrings, length = readFile.FASTAdictFromInput()
    shortest_string = shortestString(dictOfStrings)
    result = searchLongestSubstring(dictOfStrings, shortest_string)
    print "result " + result
    readFile.lineToOutput(result)
    
def shortestString(dict):
    minlength = sys.maxint
    shortest_string = ""
    for value in dict.values():
        if len(value) < minlength:
            minlength = len(value)
            shortest_string = value
    return shortest_string
            
def searchLongestSubstring(dict, shortest_string):
    queue = []
    strings = dict.values()
    strings.remove(shortest_string)
    start = Task(shortest_string)
    level = len(shortest_string)
    checked = []
    queue.append(start)
    while len(queue) != 0:
        current_task = queue.pop(0)
        substring = current_task.substring
        if level != len(substring):
            level = len(substring)
            checked = []
        else:
            if substring in checked:
                continue
        if current_task.is_substringOfAll(strings):
            return current_task.substring
        else:
            # check if append add it to the end
            if current_task.leftCropTask() != None: 
                queue.append(current_task.leftCropTask())
            if current_task.rightCropTask() != None:
                queue.append(current_task.rightCropTask())
        checked.append(substring)

class Task:
    def __init__(self, substring = None):
        self._substring = substring

    def get_substring(self):
        return self._substring
    substring = property(get_substring)

    def leftCropTask(self):
        left_substring = self._substring[1:]
        if len(left_substring) == 0:
            return None
        return Task(left_substring)

    def rightCropTask(self):
        right_substring = self._substring[:-1]
        if len(right_substring) == 0:
            return None
        return Task(right_substring)

    def is_substringOfAll(self, list):
        for string in list:
            if self._substring not in string:
                return False
        return True

        
