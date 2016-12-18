from common import *
from ffield import FElement
import ffield
from boolean import *

def FieldPow(x, n):
	p = x
	for i in range(n - 1):
		p = p * x
	return p	
	
def FuncPolynom(F, func):
	# for GF(4)
	"""
	coeffs = [FElement(F, 0)] * 4
	constants = list()
	for i in range(4):
		constants.append(FElement(F, i))
	
	coeffs[0] = func[0]
	coeffs[1] = func[1] + constants[3] * func[2] + constants[2] * func[3]
	coeffs[2] = func[1] + constants[2] * func[2] + constants[3] * func[3]
	"""
	
	#for GF(n)
	n = 2**F.n
	
	coeffs = [FElement(F, 0)] * n
	constants = list()
	for i in range(n):
		constants.append(FElement(F, i))
		
	for i in range(n - 1):
		for j in range(n):
			coeffs[i]  = coeffs[i] + func[j] * FieldPow(constants[j], n - i - 1)
	
	return coeffs
	

	
def FieldFuncToBooleanFunc(func, m):
	ans = [""] * m
	for i in range(len(func)):
		bin = ValueToBinaryStr(func[i], m)
		for j in range(m):
			ans[j] += str(bin[j])
	return ans
	
def FielFuncFourierSpectrum(F, func):
	eq = FieldFuncToBooleanFunc(func, F.n)
	fts = []
	spectrum = []
	u = "0"*F.n
	while u != "":
		sum = 0
		for j in range(1, F.n + 1):
			sum = sum + 2**(j - 1) * FourierCoeff(eq[F.n - j ], u, F.n)
		spectrum.append(sum)
		u = NextBoolVec(u)
	return spectrum
		

def FunctToFieldFunc(F, f):
	a = list()
	for i in range(len(f)):
		a.append(FElement(F, f[i]))
	return a
	
	
	