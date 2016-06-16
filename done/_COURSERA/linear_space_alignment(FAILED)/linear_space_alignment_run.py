import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import linear_space_alignment as lSA

sys.setrecursionlimit(10000)
lines = readFile.listFromInput()
v = lines[0]
w = lines[1]
out1, out2, score = lSA.linear_space_alignment_run(v, w)
answer = [str(score), out1, out2]
result = "\n".join(answer)

print result
readFile.lineToOutput(result)

#checking
#test?
sampleOutput = readFile.listFromOutput()
score_expected = int(sampleOutput[0])
out1_expected = sampleOutput[1]
out2_expected = sampleOutput[2]

if score_expected != score:
    print "score is wrong", score

if out1_expected != out1:
    print "first string is wrong"
    print out1
    print out1_expected
    c1 = 0
    # for i in xrange(0, len(out1)):
    #     if len(out1_expected) > i:
    #         if out1_expected[i] != out1[i]:
    #             c1 +=1
    #             print "[", i, "]:", out1[i], " - ", out1_expected[i]
    # print c1, "diff found"
if out2_expected != out2:
    print out2
    print out2_expected
    # print "second string is wrong"
    # c2 = 0
    # for i in xrange(0, len(out2)):
    #     if len(out2_expected) > i:
    #         if out2_expected[i] != out2[i]:
    #             c2 += 1
    #             print "[", i, "]:", out2[i], " - ", out2_expected[i]
    # print c2, "diff found"


    
