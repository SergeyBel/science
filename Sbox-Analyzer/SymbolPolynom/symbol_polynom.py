from symbol_element import *

class SPolynom:
  def __init__(self, coeffs, maxPower = 0):
    self.coeffs = coeffs
    self.maxPower = maxPower
    self.normilize()

  def normilize(self):
    zero = SElement(['0'])
    if (self.maxPower > 0 and len(self.coeffs) - 1 >= self.maxPower):
      for i in range(self.maxPower, len(self.coeffs)):
        j = (i / self.maxPower + i % self.maxPower) % self.maxPower
        if (j == 0):
            j = 1
        self.coeffs[j] += self.coeffs[i]
        self.coeffs[i] = zero
    while (len(self.coeffs) > 1  and self.coeffs[-1] == zero):
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
    return SPolynom(ans, self.maxPower)

  def __mul__(self, other):
    zero = SElement(['0'])
    lenX = len(self.coeffs)
    lenY = len(other.coeffs)
    n = lenX + lenY - 1
    ans = [zero] * n
    for i in range(0, lenX):
      for j in range(0, lenY):
        ans[i + j] += self.coeffs[i] * other.coeffs[j]
    return SPolynom(ans, self.maxPower)

  def __pow__(self, n):
    x = self
    p = SPolynom([SElement('1')], self.maxPower)
    while n: 
      if n % 2:
        p *= x
      x *= x
      n //= 2
    return p

  def toString(self):
    zero = SElement('0')
    if (len(self.coeffs) == 1 and self.coeffs[0] == zero):
      return '0'
    s = []
    for i in range(len(self.coeffs)):
      element  = self.coeffs[i]
      if element == zero:
        monom = ''
      else:
        if element.len() == 1:
          if (element == SElement('1') and i != 0):
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

  def __hash__(self):
    return hash(self.toString())

  def __eq__(self, other):
    if len(self.coeffs) != len(other.coeffs):
      return False
    for i in range(len(self.coeffs)):
      if not (self.coeffs[i] == other.coeffs[i]):
        return False
    return True

  def getCoeff(self, deg):
    if (len(self.coeffs) - 1 < deg):
      return SElement('0')
    return self.coeffs[deg]

  def copy(self):
    return SPolynom(self.coeffs, self.maxPower)

  def deg(self):
    return len(self.coeffs) - 1

  def shift(self, n):
    coeffs = [SElement('0')] * n + self.coeffs
    return SPolynom(coeffs, self.maxPower)

  def slice(self, deg):
    coeffs = self.coeffs[:deg + 1]
    return SPolynom(coeffs, self.maxPower)
