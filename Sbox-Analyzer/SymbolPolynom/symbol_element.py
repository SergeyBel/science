from symbol_monom import *

class SElement:
  def __init__(self, coeffs):
      self.coeffs = sorted(coeffs)

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

  def __str__(self):
   return self.toString()

  def __eq__(self, other):
    return self.toString() == other.toString()


