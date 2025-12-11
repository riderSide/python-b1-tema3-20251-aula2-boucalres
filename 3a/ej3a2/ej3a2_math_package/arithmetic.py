# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	if exponent < 0:
		raise ValueError("Exponent no pot ser negatiu.")
	return pow(base, exponent)
	

def square_root(num_1: float) -> float:
	if num_1 < 0:
		raise ValueError("El nombre no pot ser negatiu.")
	return math.sqrt(num_1)
