from functools import reduce, partial
from itertools import zip_longest
from operator import concat, eq, mul
from collections import ChainMap
from copy import copy
from random import randrange as rnd
from numpy import transpose

B = [list(map(copy, ['  ']*6)) for i in range(7)]
print(B)
print(B[0] is B[1])
print(B[0] is B[6])