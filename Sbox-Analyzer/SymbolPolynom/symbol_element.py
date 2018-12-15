from symbol_monom import *

class SElement:
  def __init__(self, coeffs):
    if not isinstance(coeffs, list):
      coeffs = [coeffs]
    newCoeffs = []
    for c in coeffs:
      if isinstance(c, str):
        newCoeffs.append(SMonom(c))
      else:
        newCoeffs.append(c)
    self.coeffs = newCoeffs
    self.normilize()

  def normilize(self):
    zero = SMonom('0')
    clearCoeffs = []
    for c in self.coeffs:
      if c != zero:
        clearCoeffs.append(c)
    self.coeffs = sorted(clearCoeffs)

  def len(self):
    return len(self.coeffs)

  def __add__(self, other):
    otherCoeffs = other.coeffs
    coeffs = []
    for c in self.coeffs:
      if c in otherCoeffs:
        otherCoeffs.remove(c)
      else:
        coeffs.append(c)
    for c in otherCoeffs:
      coeffs.append(c)
    return SElement(coeffs)

  def toString(self):
    if len(self.coeffs) == 0:
      return '0'
    s = []
    for c in self.coeffs:
      s.append(c.toString())
    return ' + '.join(s)

  def __mul__(self, other):
    coeffs = set()
    for a in self.coeffs:
      for b in other.coeffs:
        c = a * b
        coeffs.add(c)
    return SElement(list(coeffs))

  def __pow__(self, n):
    return self

  def __str__(self):
   return self.toString()

  def __eq__(self, other):
    return self.toString() == other.toString()


