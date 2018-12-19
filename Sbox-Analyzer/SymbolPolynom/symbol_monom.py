
class SMonom:
  def __init__(self, coeff):
    if isinstance(coeff, str):
      self.coeffs = [coeff]
    else:
      self.coeffs = coeff
    self.normilize()

  def normilize(self):
    self.coeffs = sorted(self.coeffs)

  def toString(self):
    return ''.join(self.coeffs)

  def __mul__(self, other):
    zero = SMonom('0')
    if (self == zero or other == zero):
      return zero
    one = SMonom('1')
    if (self == one):
      return other
    elif (other == one):
      return self
    else:
      coeffs = list(set(self.coeffs + other.coeffs))
      return SMonom(coeffs)

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

  def __hash__(self):
    return hash(self.toString())

  def __cmp__(self, other):
    a = self.toString()
    b = other.toString()
    if a < b:
      return -1
    elif a > b:
      return 1
    else:
      return 0
