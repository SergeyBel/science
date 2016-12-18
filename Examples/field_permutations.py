"""
Print all finite field permutations and their characteristics
"""

import sys
sys.path.append("../Boolean")
sys.path.append("../Permutation")
sys.path.append("../FField")
sys.path.append("../FFieldFunc")
sys.path.append("../FieldPolynom")

import ffield
from ffield import FElement
from  boolean import *
from field_func import *
import itertools
from permutation import *
from field_polynom import *

F = ffield.FField(2)
p = []
for i in range(2**F.n):
	p.append(i)
perms =  list(itertools.permutations(p))

c = FPolynom(F, []);
for j in range(len(perms)):
	perm = perms[j]
	fieldFunc = list(perm)
	eq = FieldFuncToBooleanFunc(fieldFunc, F.n)
	degs = ""
	for q in eq:
		degs = degs + str(Deg(q)) + ", "
	degs = "[" + degs[0:-2] + "]"
	c.FromPermutation(fieldFunc)
	cycles = GetCycles(perm)
	cycleString = StrCycles(cycles)
	cycleStruct = CycleStruct(cycles)
	print list(perm)
	print cycleString + " " + str(cycleStruct)
	print str(c) + " " + str(c.Deg())
	print degs
	print

	






