
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
    null = SMonom('0')
    if (self == null or other == null):
      return null
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
    return self.toString() == other.toString()

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
