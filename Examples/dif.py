"""
Print differential table of s-box and it's maximum value
"""

import sys
sys.path.append("../Boolean")
sys.path.append("../Cryptonalysis")
from boolean import *
from DifferentialCryptanalisys import *

n = 4
N = 2**n
s = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 2]    #present

table4 = DifferentialTable(s, n, n)
max4 = DifferentialMaximum(table4)
PrintDifferentialTable(table4, n, n)
print max4