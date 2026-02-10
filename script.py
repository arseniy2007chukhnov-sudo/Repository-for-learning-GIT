def add(a, b):
	return a + b

def divide(a, b):
	 if b == 0: 
		raise ValueError("На ноль делить нельзя")
	 else:
		return a / b
