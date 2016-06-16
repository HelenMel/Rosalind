import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

def limbLength(n, j, S):
    minValue = sys.float_info.max
    for i in xrange(0, n):
        for k in xrange(0, n):
            if k == j or i == j:
                continue
            D = float(S[i][j] + S[k][j] - S[i][k]) / 2.0
            if D < minValue:
                minValue = D
    return minValue