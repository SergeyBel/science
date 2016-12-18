#it needs to import modules from another directories
import sys
sys.path.append("../Boolean")
sys.path.append("../Permutation")
sys.path.append("../FField")
sys.path.append("../FFIeldFunc")
sys.path.append("../Cryptonalysis")
sys.path.append("../FieldPolynom")
sys.path.append("../FieldMatrix")
sys.path.append("../Algorithms")
from DifferentialCryptanalisys import *
from LineCryptoanalisys import *
import ffield
from ffield import *
from  boolean import *
from field_func import *
import itertools
from permutation import *
from field_polynom import *
from field_polynom_algorithms import *
from Berlekamp import *
from fieldmatrix import *



success = 0
fail = 0

def Test(value, answer):
	global success
	global fail
	if (value == answer):
		print "[OK]"
		success = success + 1
	else:
		print "[FAIL]"
		fail = fail + 1
		

def TestZhegalkin(f, ans):
	pol = ZhegalkinPolynom(f)
	#print StrZhegalkinPolynom(pol)
	return ans == pol
	
def TestZhegalkin1():
	print "TestZhegalkin1:",
	f = "0011"
	answer = "0010"
	Test(TestZhegalkin(f, answer), True)

	
def TestZhegalkin2():
	print "TestZhegalkin2:",
	f = "11010011"
	answer = "10111001"
	Test(TestZhegalkin(f, answer), True)
		
		
def TestWalshSpec1():
	print "TestWalshSpec1:",
	f = "1110"
	answer = [-2, -2, -2, 2]
	Test(WalshSpectrum(f, 2), answer)
		
def TestNonlineartyBool1():
	print "TestNonlineartyBool1:",
	f = "0000010100110110"
	answer = 6
	Test(NonlineartyBool(f), answer)
	
def TestIsLinearBool1():
	print "TestIsLinearBool1:",	
	f = "0000010100110110"
	Test(IsLinear(f, 4), False)
	
def TestIsLinearBool2():
	print "TestIsLinearBool2:",	
	f = "01101001"
	Test(IsLinear(f, 3), True)
	
def TestDegBool1():
	print "TestDegBool1:",	
	f = "11010011"
	answer = 3
	Test(Deg(f), answer)
	
def TestDegBool2():
	print "TestDegBool2:",	
	f = "0000010100110110"
	answer = 2
	Test(Deg(f), answer)
	
	

def FuncPolynom1():
	print "FuncPolynom1:",
	F = ffield.FField(2)
	f = [1, 3, 0, 2] #t*x^2 + 1
	answer = FPolynom(F, [FElement(F, 1), FElement(F, 0), FElement(F, 2), FElement(F, 0)], True)
	pol = FPolynom(F, [])
	pol.FromPermutation(f)
	Test(pol, answer)
	
def FieldFuncToBooleanFunc1():
	print "FieldFuncToBooleanFunc1:",
	f = [1, 3, 0, 2]
	answer = ["0101", "1100"]
	Test(FieldFuncToBooleanFunc(f, 2), answer)
	
def DegField1():
	print "DegField1:",
	F = ffield.FField(2)
	f = [1, 3, 0, 2] #t*x^2 + 1
	answer = 2
	pol = FPolynom(F, [])
	pol.FromPermutation(f)
	Test(pol.Deg(), answer)

	
def PolynomAdd1():
	print "PolynomAdd1:",
	F = FField(4)
	x = FPolynom(F, [1, 0, 5, 15])
	y = FPolynom(F, [0, 7, 8, 3])
	z = x + y
	answer = FPolynom(F, [1, 7, 13, 12])
	Test(z, answer)

def PolynomAdd2():
	print "PolynomAdd2:",
	F = FField(5)
	x = FPolynom(F, [1, 4, 17, 30])
	y = FPolynom(F, [1, 4, 17, 30])
	z = x + y
	answer = FPolynom(F, [0])
	Test(z, answer)

def PolynomSub1():
	print "PolynomSub1:",
	F = FField(4)
	x = FPolynom(F, [1, 0, 5, 15])
	y = FPolynom(F, [0, 7, 8])
	z = x - y
	answer = FPolynom(F, [1, 7, 13, 15])
	Test(z, answer)


def PolynomMul1():
	print "PolynomMul1:",
	F = FField(2)
	x = FPolynom(F, [1, 1])
	y = FPolynom(F, [1, 1])
	z = x * y
	answer = FPolynom(F, [1, 0, 1])
	Test(z, answer)

def PolynomMul2():
	print "PolynomMul2:",
	F = FField(2)
	x = FPolynom(F, [1, 0, 1])
	y = FPolynom(F, [0, 1])
	answer = FPolynom(F, [0, 1, 0, 1])
	z = x * y
	Test(z, answer)
	
def PolynomMul3():
	print "PolynomMul3:",
	F = FField(2)
	x = FPolynom(F, [1, 2, 3])
	y = FPolynom(F, [3, 2])
	answer = FPolynom(F, [3, 3, 1, 1])
	z = x * y
	Test(z, answer)
	
def PolynomMul4():
	print "PolynomMul4:",
	F = FField(2)
	x = FPolynom(F, [1, 0, 2, 3])
	y = FPolynom(F, [0])
	answer = FPolynom(F, [0])
	z = x * y
	Test(z, answer)



def PolynomDiv1():
	print "PolynomDiv1:",
	F = FField(2)
	x = FPolynom(F, [1, 0, 2])
	y = FPolynom(F, [1, 0, 2 ,3])
	answer = FPolynom(F, [0])
	z = x / y
	Test(z, answer)

def PolynomDiv2():
	print "PolynomDiv2:",
	F = FField(2)
	x = FPolynom(F, [1, 2, 3])
	y = FPolynom(F, [1, 1])
	answer = FPolynom(F, [1, 3])
	z = x / y
	Test(z, answer)

def PolynomDiv3():
	print "PolynomDiv3:",
	F = FField(6)
	x = FPolynom(F, [20, 22, 15, 17])
	y = FPolynom(F, [0, 25, 14, 18])
	c = FPolynom(F, [31, 25, 50])
	d = x * y + c
	answer = x
	z = d / y
	Test(z, answer)

def PolynomDiv4():
	print "PolynomDiv4:",
	F = FField(2)
	x = FPolynom(F, [1, 2, 2, 3])
	y = FPolynom(F, [1, 1, 1, 1])
	answer = FPolynom(F, [3])
	z = x / y
	Test(z, answer)


def PolynomMod1():
	print "PolynomMod1:",
	F = FField(2)
	x = FPolynom(F, [1, 2 ,3])
	y = FPolynom(F, [1, 1])
	answer = FPolynom(F, [0])
	z = x % y
	Test(z, answer)

def PolynomMod2():
	print "PolynomMod2:",
	F = FField(6)
	x = FPolynom(F, [20, 22, 15, 17])
	y = FPolynom(F, [0, 25, 14, 18])
	c = FPolynom(F, [31, 25, 50])
	d = x * y + c
	answer = c
	z = d % y
	Test(z, answer)

def PolynomEquilid1():
	print "PolynomEquilid1:",
	F = FField(2)
	x = FPolynom(F, [1, 0, 1])
	y = FPolynom(F, [3, 2, 1])
	z = PolynomEquilid(F, x, y)
	answer = FPolynom(F, [1, 1])
	Test(z, answer)
	
def PolynomEquilid2():
	print "PolynomEquilid2:",
	F = FField(8)
	a = FPolynom(F, [35, 22, 15, 89, 64])
	x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
	y = x * a
	z = PolynomEquilid(F, x, y)
	answer = PolynomEquilid(F, x, x)
	Test(z, answer)
	
def PolynomDerivative1():
	print "PolynomDerivative1:",
	F = FField(8)
	x = FPolynom(F, [1, 23, 45, 176, 90, 87, 65, 30])
	y = x.Derivative()
	answer = FPolynom(F, [23, 0, 176, 0, 87, 0, 30])
	Test(y, answer)

def IsLinear1():
	print "IsLinear1:",
	F = FField(2)
	x = FPolynom(F, [0, 1, 1, 0, 1, 0, 0, 0, 1])
	answer = True
	Test(x.IsLinear(), answer)

def IsLinear2():
	print "IsLinear2:",
	F = FField(4)
	x = FPolynom(F, [0, 1, 1, 3, 1, 0, 0, 0, 1])
	answer = False
	Test(x.IsLinear(), answer)

def IsAffine1():
	print "IsAffine1:",
	F = FField(2)
	x = FPolynom(F, [1, 1, 1, 0, 1, 0, 0, 0, 1])
	answer = True
	Test(x.IsAffine(), answer)

def IsAffine2():
	print "IsAffine2:",
	F = FField(4)
	x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
	answer = False
	Test(x.IsAffine(), answer)



def Berlekamp1():
	print "Berlekemp1:",
	F = FField(1)
	#x^8 + x^6 + x^4 + x^3 + x^1 = (1 + x + x^2)(1 + x + x^4 + x^5 + x^6)
	f = FPolynom(F, [1, 0, 0, 1, 1, 0, 1, 0, 1])
	x = Berlekamp(F, f)
	y = FPolynom(F, [1])
	for t in x:
		y = y * t
	Test(y, f)
	
def Berlekamp2():
	print "Berlekemp2:",
	F = FField(1)
	#x^2 + x = x * (x + 1)
	f = FPolynom(F, [0, 1, 1])
	x = Berlekamp(F, f)
	for t in x:
		y = FPolynom(F, [1])
	for t in x:
		y = y * t
	Test(y, f)
	
def Berlekamp3():
	print "Berlekemp3:",
	F = FField(1)
	#x^4 + x^3 + x = x * (x^3 + x^2 + 1)
	f = FPolynom(F, [0, 1, 0, 1, 1])
	x = Berlekamp(F, f)
	answer = False
	if (x[0] == FPolynom(F, [0, 1]) and x[1] == FPolynom(F, [1, 0, 1, 1])):
		answer = True
		
	if (x[1] == FPolynom(F, [0, 1]) and x[0] == FPolynom(F, [1, 0, 1, 1])):
		answer = True
		
	Test(answer, True)
	
def Berlekamp4():
	print "Berlekemp4:",
	F = FField(4)
	#6 + 14x^2 = 13(14+x)(14+x)
	f = FPolynom(F, [6, 0, 13])
	x = Berlekamp(F, f)
	p = FPolynom(F, [1])
	for t in x:
		p = p * t
	Test(f, p)
	
def IsPermutaion1():
	print "IsPermutation1:",
	p = [1, 4, 6, 3, 7, 2, 5, 0]
	ans = True
	x = IsPermutation(p)
	Test(x, ans)

def IsPermutaion2():
	print "IsPermutation2:",
	p = [1, 1, 1, 1, 1, 1, 1, 1]
	ans = False
	x = IsPermutation(p)
	Test(x, ans)
	
def TestIsPermutation1():
	print "TestIsPermutation1:",
	f = [0, 1, 2 ,3]
	Test(IsPermutation(f), True)
	
def TestIsPermutation2():
	print "TestIsPermutation2:",
	f = [0, 1, 1, 2]
	Test(IsPermutation(f), False)
	
def GetCycles1():
	print "GetCycles1:",
	f = [3, 1, 5, 0, 4, 2]
	answer = [2, 2, 0, 0, 0, 0]
	c = GetCycles(f)
	st = CycleStruct(c)
	Test(st, answer)
	
def InvPermutation1():
	print "InvPermutation1:",
	f = [5, 3, 6, 1, 2, 7, 0, 4]
	ans = [6, 3, 4, 1, 7, 0, 2, 5]
	inv = InvPermutation(f)
	Test(inv, ans)
	
def NextPermutation1():
	print "NextPermutation1:",
	f = [0, 1, 7, 6, 5, 4, 3, 2]
	ans = [0, 2, 1, 3, 4, 5, 6, 7]
	next = NextPermutation(f)
	Test(next, ans)
	
def PermCompose1():
	print "PermCompose1:",
	f = [0, 1, 7, 6, 5, 4, 3, 2]
	g = [7, 1, 6, 5, 4, 3, 2, 0]
	ans = [7, 1, 0, 2, 3, 4, 5, 6]
	next = PermCompose(g, f)
	Test(next, ans)
	

	
def MatrixGetRow1():
	print "MatrixGetRow1:",
	F = FField(4)
	m = FMatrix(F, 3, 3)
	m.Ident()
	r = m.GetRow(1)
	ans = [FElement(F, 0), FElement(F, 1), FElement(F, 0)]
	Test(r, ans)

def MatrixGetColumn1():
	print "MatrixGetColumn1:",
	F = FField(4)
	m = FMatrix(F, 5, 5)
	m.Ident()
	r = m.GetColumn(0)
	ans = [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 0)]
	Test(r, ans)


	
def BoolSuite():
	TestZhegalkin1()
	TestZhegalkin2()
	TestWalshSpec1()
	TestNonlineartyBool1()
	TestDegBool1()
	TestDegBool2()
	TestIsLinearBool1()
	TestIsLinearBool2()


	
	
def FieldSuite():
	FuncPolynom1()
	FieldFuncToBooleanFunc1()
	DegField1()
	
def PolynomSuite():
	PolynomAdd1()
	PolynomAdd2()
	PolynomSub1()
	PolynomMul1()
	PolynomMul2()
	PolynomMul3()
	PolynomMul4()
	PolynomDiv1()
	PolynomDiv2()
	PolynomDiv3()
	PolynomDiv4()
	PolynomMod1()
	PolynomMod2()
	PolynomEquilid1()
	PolynomEquilid2()
	PolynomDerivative1()
	IsLinear1()
	IsLinear2()
	IsAffine1()
	IsAffine2()
	
def AlgorithmSuite():
	Berlekamp1()
	Berlekamp2()
	Berlekamp3()
	Berlekamp4()
	
def PermutationSuite():
	TestIsPermutation1()
	TestIsPermutation2()
	IsPermutaion1()
	IsPermutaion2()
	GetCycles1()
	InvPermutation1()
	NextPermutation1()
	PermCompose1()
	
def MatrixSuite():
	MatrixGetRow1()
	MatrixGetColumn1()
	

BoolSuite()
FieldSuite()
PolynomSuite()
AlgorithmSuite()
PermutationSuite()
MatrixSuite()

print
print "OK: ", success
print "FAIL: ", fail


