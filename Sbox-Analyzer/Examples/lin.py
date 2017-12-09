"""
Print linear table of s-box and it's maximum value
"""


import sys
sys.path.append("../Boolean")
sys.path.append("../Cryptonalysis")
from boolean import *
from LineCryptoanalisys import *		


n = 4
N = 2**n
s = [3, 8, 	15, 	1, 	10, 	6, 	5, 	11, 	14, 	13, 	4, 	2, 	7 ,	0, 	9, 	12]    #serpent 1
s = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 2]    #present

links4 = GenerateLineLinks(n, n)
table4 = LinearApproximationTable(s, n, n, links4)
max4 = LinearApproximateMaximum(table4)
PrintLinearApproximationTable(table4, n, n)
print max4






	













		


			
			


