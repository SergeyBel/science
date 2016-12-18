	
def ValueToBinaryStr(value, length):
	s = bin(value)[2:]
	s  = "0" * (length - len(s)) + s
	return s

def BinaryStrToValue(str):
	return int(str, 2)

def BooleanFuncToFieldFunc(equations):
	res = list()
	for i in range(0, len(equations[0])):
		s = ""
		for j in range(0, len(equations)):
			s = s + equations[j][i]
		res.append(BinaryStrToValue(s))
	return res
	
def SwapArr(a, i, j):
	c = a[i]
	a[i] = a[j]
	a[j] = c