from symbol_element import *

class SPolynom:
  def __init__(self, coeffs):
    self.coeffs = coeffs
    self.normilize()

  def normilize(self):
    x = self.coeffs
    NullElem = SElement([])
    while (len(self.coeffs) > 1  and self.coeffs[-1] == NullElem):
      del self.coeffs[-1]

  def __add__(self, other):
    lenX = len(self.coeffs)
    lenY = len(other.coeffs)
    ans = []
    if lenX > lenY:
      c = self.coeffs
      m = lenX
      n = lenY
    else:
      c = other.coeffs
      m = lenY
      n = lenX
    
    for i in range(n):
      ans.append(self.coeffs[i] + other.coeffs[i])
    ans[n:m] = c[n:m]
    return SPolynom(ans)

  def __mul__(self, other):
    NullElement = SElement([])
    lenX = len(self.coeffs)
    lenY = len(other.coeffs)
    n = lenX + lenY - 1
    ans = [NullElement] * n
    for i in range(0, lenX):
      for j in range(0, lenY):
        ans[i + j] += self.coeffs[i] * other.coeffs[j]
    return SPolynom(ans)

  def __pow__(self, n):
    p = SPolynom(self.coeffs)
    for i in range(n - 1):
      p = p * self
    return p


  def toString(self):
    if (len(self.coeffs) == 1 and self.coeffs[0] == SElement([])):
      return '0'
    s = []
    for i in range(len(self.coeffs)):
      element  = self.coeffs[i]
      if element.len() == 0:
        monom = ''
      else:
        if element.len() == 1:
          if (element == SElement('1')):
            coeff = ''
          else:
            coeff = self.coeffs[i].toString()
        else:
          coeff = '(' + self.coeffs[i].toString() + ')'
        if (i  == 0):
          power = ''
        elif i == 1:
          power = 'X'
        else:
          power = 'X^' + str(i)
        monom = coeff + power
        s.append(monom)
    return ' + '.join(s)

  def __str__(self):
    return self.toString()

  def __eq__(self, other):
    return self.coeffs == other.coeffs