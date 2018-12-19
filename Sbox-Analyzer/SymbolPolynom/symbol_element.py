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
    coeffs = list()
    for a in self.coeffs:
      for b in other.coeffs:
        c = a * b
        if c in coeffs:
          coeffs.remove(c)
        else:
          coeffs.append(c)
    return SElement(list(coeffs))

  def __pow__(self, n):
    return self

  def __str__(self):
   return self.toString()

  def __eq__(self, other):
    if len(self.coeffs) != len(other.coeffs):
      return False
    for i in range (len(self.coeffs)):
      if self.coeffs[i] != other.coeffs[i]:
        return False
    return True


