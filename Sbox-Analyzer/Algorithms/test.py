#it needs to import modules from another directories
import sys
sys.path.append("../Boolean")
sys.path.append("../FField")
sys.path.append("../FFIeldFunc")
sys.path.append("../Cryptonalysis")
sys.path.append("../FieldPolynom")
from DifferentialCryptanalisys import *
from LineCryptoanalisys import *
import ffield
from ffield import FElement
from  boolean import *
from field_func import *
import itertools
from field_polynom import *
from Berlekamp import *

n = 4
F = ffield.FField(n)

sbox = [3, 	8, 	15, 	1, 	10, 	6, 	5, 	11, 	14, 	13, 	4, 	2, 	7, 	0, 	9, 	12]
s = FPolynom(F, [])
s.FromPermutation(sbox)
print s
d = Berlekamp(F, s)
for t in d:
	print t