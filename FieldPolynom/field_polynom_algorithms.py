from field_polynom import *

def PolynomEquilid(F, x, y):
	if (x.Deg() < y.Deg()):
		f = y.Copy()
		g = x.Copy()
	else:
		f = x.Copy()
		g = y.Copy()
		
	polNull = FPolynom(F, [0])
	
	if g == polNull:
		return f
		
	while True:
		r = f % g
		if r == polNull:
			break
		f = g
		g = r
	g.Normalize()
	return g
	
def PolynomPow(F, x, n):
	p = FPolynom(F, [1])
	for i in range(n):
		p = p * x
	return p
	
def RandomFPolynom(F, n):
	N = 2**F.n
	coeffs = list()
	for i in range(n):
		coeffs.append(randint(0, N - 1))
	coeffs.append(randint(1, N - 1))
	return FPolynom(F, coeffs)
	
def NextCoeffs(F, c):
	N = FElement(F, 2**F.n - 1)
	i = 0
	n = len(c)
	while (i < n) and (c[i] == N):
		i = i + 1
	if i == n:
		return False
	c[i] = FElement(F, c[i].f + 1)
	for j in range(0, i):
		c[j] = FElement(F, 0)
	return c
	
def NextLinearPolynom(F, f):
	coeffs = [FElement(F,0)] * F.n
	for i in range(F.n):
		if (2**i < len(f.c)):
			coeffs[i] = f.c[2**i]
	nextCoeffs = NextCoeffs(F, coeffs)
	if nextCoeffs == False:
		return False
	twoPower = 0
	
	coeffs = [FElement(F,0)] * 2**F.n
	for i in range(2**F.n):
		if (i == 2**twoPower):
			coeffs[i] = nextCoeffs[twoPower]
			twoPower += 1
	g = FPolynom(F, coeffs, True)
	return g
	
def NextAffinePolynom(F, f):
	N = 2**F.n - 1
	g = f.Copy()
	c = g.c[0]
	if c == FElement(F, N):
		g.c[0] = FElement(F, 0)
		g = NextLinearPolynom(F, g)
	else:
		g.c[0] = FElement(F, g.c[0].f + 1)
	return g
		
	


	