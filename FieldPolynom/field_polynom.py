
import sys
sys.path.append("../Boolean")
sys.path.append("../FField")
sys.path.append("../FFIeldFunc")
sys.path.append("../Cryptonalysis")
from DifferentialCryptanalisys import *
from LineCryptoanalisys import *
from ffield import *

from  boolean import *
from field_func import *
import itertools
from random import randint

#polynom a_0+a_1*X+...+a_n-1*X^n = (a_0, a_1,...,a_n-1)



	
def DegPolynom(F, coeffs):
	i = len(coeffs) - 1
	NullElem = FElement(F, 0)
	while  i >= 0 and coeffs[i] == NullElem:
		i = i - 1
	return i
	
def StrPolynom(F, coeffs, polynom = False):
	s = ""
	if (DegPolynom(F, coeffs) == -1):
		return "0"
	for i in range(len(coeffs)):
		if i == 0:
			degree = ""
		elif i == 1:
			degree = "*X"
		else:
			degree = "*X^" + str(i)
			
		if i != 0 and s != "":
			sign = "+ "
		else:
			sign = ""
		if not (coeffs[i] == FElement(F, 0)):
			if polynom == True:
				s = s + sign + "(" + str(coeffs[i]) + ")" + degree + " "
			else:
				s = s + sign + str(coeffs[i].f) + degree + " "
	return s

def PolynomCorrect(F, x):
	NullElem = FElement(F, 0)
	while (len(x) > 1  and x[-1] == NullElem):
		del x[-1]
	return x


def PolynomAdd(F, x, y): 
	lenX = len(x)
	lenY = len(y)
	if lenX > lenY:
		ans = x[:]
		n = lenY
	else:
		ans = y[:]
		n = lenX
		
	for i in range(n):
		ans[i] = x[i] + y[i]
	return PolynomCorrect(F, ans)
	
def PolynomSub(F, x, y):
	return PolynomAdd(F, x, y)
	
def PolynomMul(F, x, y):
	NullElement = FElement(F, 0)
	lenX = len(x)
	lenY = len(y)
	n = lenX + lenY - 1
	ans = [NullElement] * n
	for i in range(0, lenX):
		for j in range(0, lenY):
			ans[i + j] += x[i] * y[j]
	return PolynomCorrect(F, ans)
	
def PolynomDiv(F, x, y):

	NullElement = FElement(F, 0)
	degX = DegPolynom(F, x)
	degY = DegPolynom(F, y)

	n = max(len(x) - len(y) + 1, 1)
	divisor = [NullElement] * n
	g = x[:]
	while (degX >= degY):
		p = degX - degY    #divisor degree
		c = g[-1] / y[-1] #divisor coeff
		d = [NullElement] * (p + 1)
		d[-1] = c
		divisor = PolynomAdd(F, divisor, d)
		z = PolynomMul(F, y, d)
		g = PolynomSub(F, g, z)
		degX = DegPolynom(F, g)
	return (PolynomCorrect(F, divisor), PolynomCorrect(F, g))
	
def PolynomNormalize(F, x):
	c = x[-1]
	normalizator = [FElement(F, F.Inverse(c.f))]
	z = PolynomMul(F, x, normalizator)
	return z


	

	
def FPow(F, x, n):
	p = FElement(F, 1)
	for i in range(n):
		p = p * x
	return p


class FPolynom:
	def __init__(self, field, coeffs, isField = False):
		self.field = field
		if (isField == False):
			self.c = []
			for i in range(len(coeffs)):
				self.c.append(FElement(field, coeffs[i]))
		else:
			self.c = coeffs[:]
		PolynomCorrect(self.field, self.c)
		
			
	def __add__(self, other):
		return FPolynom(self.field, PolynomAdd(self.field, self.c, other.c), True)
		
	def __sub__(self, other):
		return FPolynom(self.field, PolynomSub(self.field, self.c, other.c), True)
		
	def __mul__(self, other):
		return FPolynom(self.field, PolynomMul(self.field, self.c, other.c), True)

	def __div__(self, other):
		(divisor, rest) = PolynomDiv(self.field, self.c, other.c)  # x / y
		return FPolynom(self.field, divisor, True)
		
	def __mod__(self, other):
		(divisor, rest) = PolynomDiv(self.field, self.c, other.c)  # x % y
		return FPolynom(self.field, rest, True)
		
	def __len__(self):
		return len(self.c)


	def __str__(self):
		return StrPolynom(self.field, self.c)
		
	def __eq__(self,other):
		return self.field == other.field and self.c == other.c
		
	def __hash__(self):
		s = ""
		for i in range(len(self.c)):
			s = s + str(self.c[i])
		t = tuple(s)
		return hash( (self.field, t) )
		
	def Correct(self):
		return FPolynom(self.field, PolynomCorrect(self.field, self.c), True)
	
	def Deg(self):
		return DegPolynom(self.field, self.c)
	
	def Normalize(self):
		self.Correct()
		self.c = PolynomNormalize(self.field, self.c)
		
	def Derivative(self):
		"""
		f = a_0+a_1*X+...+a_n-1*X^n
		f' = a_1+2*a_2*X+...+(n-1)a_n-1*X^(n-1)
		n * a = a + a + a + ... + a, n times
		"""
		t = self.Copy()
		t.c.pop(0)
		for i in range(len(t.c)):
			k = FElement(t.field, 0)
			for j in range(i + 1):
				k = k + t.c[i]
			t.c[i] = k
		return t.Correct()
		
	def Copy(self):
		return FPolynom(self.field, self.c[:], True)
		
	def Value(self, x):
		v = FElement(self.field, 0)
		for i in range(len(self.c)):
			v = v + self.c[i] * FPow(self.field, x, i)
		return v
		
	def Values(self):
		N = 2 ** self.field.n
		values = []
		for i in range(N):
			values.append(self.Value(FElement(self.field, i)))
		return values
			

		

