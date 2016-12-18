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

F = ffield.FField(3)
p = []
for i in range(2**F.n):
	p.append(i)
perms =  list(itertools.permutations(p))


for j in range(len(perms)):
	perm = perms[j]
	fieldFunc = list(perm)
	eq = FieldFuncToBooleanFunc(fieldFunc, F.n)
	degs = ""
	for q in eq:
		degs = degs + str(Deg(q)) + ", "
	degs = "[" + degs[0:-2] + "]"
	for i in range(len(fieldFunc)):
		fieldFunc[i] = FElement(F, fieldFunc[i])
	c =  FuncPolynom(F, fieldFunc)
	cycles = GetCycles(perm)
	cycleString = StrCycles(cycles)
	cycleStruct = CycleStruct(cycles)
	print list(perm)
	print cycleString + " " + str(cycleStruct)
	print StrPolynom(F, c) + " " + str(DegPolynom(F, c))
	print degs
	print

	


"""
fieldFunc = [0,1,2,3,4,5,6,7]

for i in range(8):
	fieldFunc[i] = F.Add(F.Multiply(i, i), i)    #y^2 + y
cycles = GetCycles(fieldFunc)
for i in range(len(fieldFunc)):
	fieldFunc[i] = FElement(F, fieldFunc[i])
c =  FuncPolynom(F, fieldFunc)
print c
	
print StrPolynom(F, c) + " " + str(DegPolynom(F, c))
"""





