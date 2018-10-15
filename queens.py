#!/usr/local/bin/python3

# 8 Queens
# from http://code.activestate.com/recipes/576647/

from itertools import permutations

n = 8
cols = range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print ("\n".join('#' * i + 'Q' + '#' * (n-i-1) for i in vec) + '\n')
