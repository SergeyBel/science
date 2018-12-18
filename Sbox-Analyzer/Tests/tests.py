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
sys.path.append("../SymbolPolynom")
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
from symbol_polynom import *



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

def TestIsMonotone1():
	print "TestIsMonotone1:",	
	f = "00010111"
	answer = True
	Test(IsMonotone(f), answer)

def TestIsMonotone2():
	print "TestIsMonotone2:",	
	f = "0110"
	answer = False
	Test(IsMonotone(f), answer)

def TestIsMonotone3():
	print "TestIsMonotone3:",	
	f = "1011"
	answer = False
	Test(IsMonotone(f), answer)
	
	

def FuncPolynom1():
	print "FuncPolynom1:",
	F = ffield.FField(2)
	f = [1, 3, 0, 2] #t*x^2 + 1
	answer = FPolynom(F, [FElement(F, 1), FElement(F, 0), FElement(F, 2), FElement(F, 0)], True)
	pol = FPolynom(F, [])
	pol.FromPermutation(f)
	Test(pol, answer)

def FuncPolynom2():
	print "FuncPolynom2:",
	F = ffield.FField(2)
	f = [1, 2, 2, 0] #x^3 + x^2 + x(t + 1) + 1
	answer = FPolynom(F, [1, 3, 1, 1])
	pol = FPolynom(F, [])
	pol.FromPermutation(f)
	Test(pol, answer)

def FuncPolynom3():
	print "FuncPolynom3:",
	F = ffield.FField(2)
	f = [1, 1, 1, 1] 
	answer = f
	pol = FPolynom(F, [])
	pol.FromPermutation(f)
	Test(pol.Values(False), answer)


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

def DualBasis1():
	print "DualBasis1:",
	F = FField(4)
	dualBasis = DualBasis(F)
	answer = [FElement(F, 9), FElement(F, 4), FElement(F, 2), FElement(F, 1)]
	Test(dualBasis, answer)

	
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

def PolynomRank1():
	print "PolynomRank1:",
	F = FField(4)
	x = FPolynom(F, [3, 1, 1, 0, 1, 0, 0, 2, 1])
	answer = 6
	Test(x.Rank(), answer)

def PolynomReduce1():
	print "PolynomReduce1:",
	F = FField(2)
	f = FPolynom(F, [1, 1, 1, 1, 1])
	f.Reduce()
	answer = FPolynom(F,[1, 0, 1, 1])
	Test(f, answer)

def PolynomReduce2():
	print "PolynomReduce2:",
	F = FField(4)
	f = FPolynom(F, [0, 0, 0, 0, 4, 13, 3, 7, 10, 13, 8, 5, 12, 4, 15, 1, 8, 14, 10, 11, 12, 11, 11, 0, 2, 9, 13, 0, 14, 0, 0, 0, 2])
	f.Reduce()
	answer = FPolynom(F, [0, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1, 8, 12, 10, 15, 1])
	Test(f, answer)

def FromZhekalkinPolynom1():
	print "FromZhekalkinPolynom1:",
	F = FField(2)
	f = "0011"
	zhekalkin = ZhegalkinPolynom(f)
	g = FromZhekalkinPolynom(F, zhekalkin)
	answer = FPolynom(F, [0, 1, 1])
	Test(g, answer)

def FromZhekalkinPolynom2():
	print "FromZhekalkinPolynom2:",
	F = FField(2)
	f = "0001"
	zhekalkin = ZhegalkinPolynom(f)
	g = FromZhekalkinPolynom(F, zhekalkin)
	answer = FPolynom(F, [0, 2, 3, 1])
	Test(g, answer)

def FromZhekalkinPolynom3():
	print "FromZhekalkinPolynom3:",
	F = FField(2)
	f = "0110"
	zhekalkin = ZhegalkinPolynom(f)
	g = FromZhekalkinPolynom(F, zhekalkin)
	answer = FPolynom(F, [0, 2, 3])
	Test(g, answer)

def FromZhekalkinPolynom4():
	print "FromZhekalkinPolynom4:",
	F = FField(4)
	f = "0"*15 + "1"
	zhekalkin = ZhegalkinPolynom(f)
	g = FromZhekalkinPolynom(F, zhekalkin)
	answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	Test(g.Values(False), answer)

def PolynomPow1():
	F = FField(2)
	x = PolynomPow(F, FPolynom(F, [0, 1, 1]), 2)
	answer = FPolynom(F, [0, 0, 1, 0, 1])
	Test(x, answer)

def PolynomPow2():
	F = FField(2)
	x = PolynomPow(F, FPolynom(F, []), 1)
	answer = FPolynom(F, [])
	Test(x, answer)

def PolynomPow3():
	F = FField(2)
	x = PolynomPow(F, FPolynom(F, []), 0)
	answer = FPolynom(F, [1])
	Test(x, answer)

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

def MatrixInverse():
	print "MatrixInverse:",

	F = FField(2)
	m = FMatrix(F, 4, 4)
	m.SetRow(0, [FElement(F, 0), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
	m.SetRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
	m.SetRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
	m.SetRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
	inv = m.Inverse()
	ans = FMatrix(F, 4, 4)
	ans.SetRow(0, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 1)])
	ans.SetRow(1, [FElement(F, 0), FElement(F, 0), FElement(F, 1), FElement(F, 0)])
	ans.SetRow(2, [FElement(F, 0), FElement(F, 1), FElement(F, 0), FElement(F, 0)])
	ans.SetRow(3, [FElement(F, 1), FElement(F, 0), FElement(F, 0), FElement(F, 0)])
	Test(inv, ans)

def SMonomMul1():
	print 'SMonomMul1',
	a = SMonom('a')
	b = SMonom('b')
	s = a * b
	ans = SMonom('ab')
	Test(ans, s)

def SMonomMul2():
	print 'SSMonomMul2',
	a = SMonom('a')
	b = SMonom('b')
	c = SMonom('c')
	s = c * a * b
	ans = SMonom('abc')
	Test(ans, s)

def SMonomMul3():
	print 'SSMonomMul3',
	a = SMonom('1')
	b = SMonom('b')
	s =  a * b
	ans = SMonom('b')
	Test(ans, s)

def SMonomMul4():
	print 'SSMonomMul4',
	a = SMonom('0')
	b = SMonom('b')
	s =  a * b
	ans = SMonom('0')
	Test(ans, s)

def SMonomMul5():
	print 'SSMonomMul5',
	a = SMonom('a')
	b = SMonom('1')
	s =  a * b
	ans = SMonom('a')
	Test(ans, s)

def SMonomMul6():
	print 'SSMonomMul6',
	a = SMonom('a')
	b = SMonom('0')
	s =  a * b
	ans = SMonom('0')
	Test(ans, s)

def SElementAdd1():
	print 'SElementAdd1',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('b')])
	ans = SElement([SMonom('a'), SMonom('b')])
	Test(ans, a + b)

def SElementAdd2():
	print 'SElementAdd2',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('b')])
	c = SElement([SMonom('c')])
	ans = SElement([SMonom('a'), SMonom('b'), SMonom('c')])
	Test(ans, c + a + b)

def SElementAdd3():
	print 'SElementAdd3',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('a')])
	ans = SElement(['0'])
	Test(ans, a + b)

def SElementAdd4():
	print 'SElementAdd4',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('0')])
	ans = SElement(['a'])
	Test(ans, a + b)

def SElementAdd5():
	print 'SElementAdd5',
	a = SElement([SMonom('1')])
	b = SElement([SMonom('a')])
	ans = SElement(['a', '1'])
	Test(ans, a + b)

def SElementAdd6():
	print 'SElementAdd6',
	a = SElement('a1')
	b = SElement('a2')
	ans = SElement(['a1', 'a2'])
	Test(ans, a + b)

def SElementMul1():
	print 'SElementMul1',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('a')])
	ans = SElement([SMonom('a')])
	Test(ans, a * b)

def SElementMul2():
	print 'SElementMul2',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('b')])
	ans = SElement([SMonom('ab')])
	Test(ans, a * b)

def SElementMul3():
	print 'SElementMul3',
	a = SElement([SMonom('a')])
	b = SElement([SMonom('b'), SMonom('c')])
	ans = SElement([SMonom('ab'), SMonom('ac')])
	Test(ans, a * b)

def SElementMul4():
	print 'SElementMul4',
	a = SElement([SMonom('1')])
	b = SElement([SMonom('b')])
	ans = SElement([SMonom('b')])
	Test(ans, a * b)

def SElementMul5():
	print 'SElementMul5',
	a = SElement([SMonom('0')])
	b = SElement([SMonom('b')])
	ans = SElement([SMonom('0')])
	Test(ans, a * b)

def SPolynomAdd1():
	print 'SPolynomAdd1',
	a = SPolynom([SElement('a')])
	b = SPolynom([SElement('b')])
	ans = SPolynom([SElement([SMonom('a'), SMonom('b')])])
	Test(ans, a + b)

def SPolynomAdd2():
	print 'SPolynomAdd2',
	a = SPolynom([SElement('a'), SElement('c')])
	b = SPolynom([SElement('a')])
	ans = SPolynom([SElement([]), SElement('c')])
	Test(ans, a + b)

def SPolynomAdd3():
	print 'SPolynomAdd3',
	a = SPolynom([SElement('a')])
	b = SPolynom([SElement('a')])
	ans = SPolynom([SElement('0')])
	Test(ans, a + b)

def SPolynomAdd4():
	print 'SPolynomAdd4',
	a = SPolynom([SElement('a'), SElement('b'), SElement('c')])
	b = SPolynom([SElement('b'), SElement('c'), SElement('a')])
	ans = SPolynom([SElement(['a', 'b']), SElement(['b', 'c']), SElement(['a', 'c'])])
	Test(ans, a + b)

def SPolynomMul1():
	print 'SPolynomMul1',
	a = SPolynom([SElement('a')])
	b = SPolynom([SElement('b')])
	ans = SPolynom([SElement(['ab'])])
	Test(ans, a * b)

def SPolynomMul2():
	print 'SPolynomMul2',
	a = SPolynom([SElement('a')])
	b = SPolynom([SElement('a')])
	ans = SPolynom([SElement(['a'])])
	Test(ans, a * b)

def SPolynomMul3():
	print 'SPolynomMul4',
	a = SPolynom([SElement('a'), SElement('b')])
	b = SPolynom([SElement('c')])
	ans = SPolynom([SElement(['ac']), SElement(['bc'])])
	Test(ans, a * b)

def SPolynomMul4():
	print 'SPolynomMul4',
	a = SPolynom([SElement('a'), SElement('b')])
	b = SPolynom([SElement('c'), SElement('d')])
	ans = SPolynom([SElement(['ac']), SElement([SMonom('bc'), SMonom('ad')]), SElement(['bd'])])
	Test(ans, a * b)

def SPolynomMul5():
	print 'SPolynomMul5',
	a = SPolynom([SElement('a'), SElement('1')])
	b = SPolynom([SElement('c')])
	ans = SPolynom([SElement(['ac']), SElement(['c'])])
	Test(ans, a * b)

def SPolynomMul6():
	print 'SPolynomMul6',
	a = SPolynom([SElement('a'), SElement('1')])
	b = SPolynom([SElement('a'), SElement('0'), SElement('1')])
	ans = SPolynom([SElement(['a']), SElement(['a']), SElement(['a']), SElement(['1']),])
	Test(ans, a * b)

def SPolynoPow1():
	print 'SPolynomPow1',
	a = SPolynom([SElement('a')])
	ans = a
	Test(ans, a ** 2)

def SPolynoPow2():
	print 'SPolynomPow2',
	a = SPolynom([SElement('a'), SElement('b')])
	ans = SPolynom([SElement('a'), SElement([]), SElement('b')])
	Test(ans, a ** 2)

def SPolynomExpr1():
	print 'SPolynomExpr1',
	a = SPolynom([SElement('a'), SElement('1')])
	b = SPolynom([SElement('a'), SElement('b'), SElement('1')])
	ans = SPolynom([SElement('a'), SElement('a'), SElement(['ab']), SElement('b'), SElement('a'), SElement('1')])	
	Test(ans, a * b ** 2)

def SPolynomShift1():
	print 'SPolynomShift1',
	a = SPolynom([SElement('a'), SElement('1')])
	ans = SPolynom([SElement('0'),SElement('a'), SElement('1')])
	Test(ans, a.shift(1))

def SPolynomShift2():
	print 'SPolynomShift2',
	a = SPolynom([SElement('a'), SElement('1')])
	ans = SPolynom([SElement('0'), SElement('0'), SElement('a'), SElement('1')])
	Test(ans, a.shift(2))

def SPolynomShift3():
	print 'SPolynomShift3',
	a = SPolynom([SElement('a'), SElement('1')])
	ans = a
	Test(a, a.shift(0))

	
def BoolSuite():
	TestZhegalkin1()
	TestZhegalkin2()
	TestWalshSpec1()
	TestNonlineartyBool1()
	TestDegBool1()
	TestDegBool2()
	TestIsLinearBool1()
	TestIsLinearBool2()
	TestIsMonotone1()
	TestIsMonotone2()
	TestIsMonotone3()


	
	
def FieldSuite():
	FuncPolynom1()
	FuncPolynom2()
	FuncPolynom3()
	FieldFuncToBooleanFunc1()
	DegField1()
	DualBasis1()
	
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
	PolynomRank1()
	PolynomReduce1()
	PolynomReduce2()
	FromZhekalkinPolynom1()
	FromZhekalkinPolynom2()
	FromZhekalkinPolynom3()
	FromZhekalkinPolynom4()
	PolynomPow1()
	PolynomPow2()
	PolynomPow3()
	
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
	MatrixInverse()

def SMonomSuite():
	SMonomMul1()
	SMonomMul2()
	SMonomMul3()
	SMonomMul4()
	SMonomMul5()
	SMonomMul6()

def SElementSuite():
	SElementAdd1()
	SElementAdd2()
	SElementAdd3()
	SElementAdd4()
	SElementAdd5()
	SElementMul1()
	SElementMul2()
	SElementMul3()
	SElementMul4()
	SElementMul5()
	SElementAdd6()

def SPolynomSuite():
	SPolynomAdd1()
	SPolynomAdd2()
	SPolynomAdd3()
	SPolynomAdd4()
	SPolynomMul1()
	SPolynomMul2()
	SPolynomMul3()
	SPolynomMul4()
	SPolynomMul5()
	SPolynomMul6()
	SPolynoPow1()
	SPolynoPow2()
	SPolynomExpr1()
	SPolynomShift1()
	SPolynomShift2()
	SPolynomShift3()
	

BoolSuite()
FieldSuite()
PolynomSuite()
AlgorithmSuite()
PermutationSuite()
MatrixSuite()
SMonomSuite()
SElementSuite()
SPolynomSuite()

print
print "OK: ", success
print "FAIL: ", fail

