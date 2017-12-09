"""
Print finite field multiply table
"""

import sys
sys.path.append("../Boolean")
sys.path.append("../FField")
sys.path.append("../FFieldFunc")
import ffield
from ffield import FElement
from  boolean import *
from field_func import *
import itertools

n = 3
F = ffield.FField(n)

"""
n = 3
F = ffield.FField(n, 13, 0)
#To change irredible polynomial see ffield.py
"""


for x in range (1, 2**n):
	for y in range (1, 2**n):
		print '{:4}'.format(F.Multiply(x, y)),
	print

		