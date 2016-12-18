#it needs to import modules from another directories
import sys
sys.path.append("../Boolean")
sys.path.append("../Permutation")
sys.path.append("../FField")
sys.path.append("../FFIeldFunc")
sys.path.append("../FieldPolynom")
sys.path.append("../Cryptonalysis")
from DifferentialCryptanalisys import *
from LineCryptoanalisys import *
import ffield
from ffield import FElement
from  boolean import *
from field_func import *
import itertools
from permutation import *
from field_polynom import *


n = 4
F = ffield.FField(n)


sbox = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 15, 14]






print "S-box:"
print sbox
print


print "Differential table:"
table = DifferentialTable(sbox, n, n)
max =  DifferentialMaximum(table)
PrintDifferentialTable(table, n, n)
print "Differential max = " + str(max)
print


"""
print "Linear table:"
links = GenerateLineLinks(n, n)
table = LinearApproximationTable(sbox, n, n, links)
max = LinearApproximateMaximum(table)
PrintLinearApproximationTable(table, n, n)
print "Linear max = " + str(max)
print
"""
fieldFunc = [0] * len(sbox)

eq = FieldFuncToBooleanFunc(sbox, F.n)
#PrintEquations(eq)

for i in range(len(sbox)):
	fieldFunc[i] = FElement(F, sbox[i])
c =  FuncPolynom(F, fieldFunc)

cycles = GetCycles(sbox)
cycleString = StrCycles(cycles)
cycleStruct = CycleStruct(cycles)

print '{:60s}'.format("Boolean function:")  + '{:10s}'.format("Degree") + '{:7s}'.format("Nonlinearty")
print


#Zhekalkin functions need tests
for i in range (len(eq)):
	print str(i + 1) + ": " + '{:60s}'.format(StrZhegalkinPolynom(ZhegalkinPolynom(eq[i]))) + '{:10s}'.format(str(Deg(eq[i]))) + '{:7s}'.format(str(NonlineartyBool(eq[i])))
	

print
print "Field polymom:"
print '{:140s}'.format(StrPolynom(F, c, False))
print
print "Field polynom deg:"
print '{:2s}'.format(str(DegPolynom(F, c)))
print
print "Cycle struct:"
print '{:20s}'.format(cycleString)
print
print "Cycles amount:"
print str(cycleStruct) 







