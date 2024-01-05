# ecc/utils/ecc_utils.py
from fractions import Fraction

def find_frac(decimal_value):
    fraction_obj = Fraction(decimal_value).limit_denominator()
    return fraction_obj

def mod_inverse(a, m):
    return pow(a, -1, m)

def tonelli_shanks(p, n):
	
	if n % p == 0:
		return 0

	if not check_residue(n, p):
		print("This value of n is not a quadratic residue.")
		return None
	else:
		print("This value of n is a quadratic residue.")

	if p % 4 == 3:
		return pow(n, (p + 1)//4, p)
	
	Q = p - 1
	S = 0
	while Q % 2 == 0:
		S += 1
		Q //= 2

	z = 2
	while check_residue(z, p):
		z += 1

	M = S
	c = pow(z, Q, p)
	t = pow(n, Q, p)
	R = pow(n, (Q + 1)//2, p)

	while t != 1:

		i = 0
		temp = t 
		while temp != 1:
			i += 1
			temp = (temp * temp) % p
		
		pow2 = 2 ** (M - i - 1)
		b = pow(c, pow2, p)
		M = i
		c = (b * b) % p
		t = (t * b * b) % p
		R = (R * b) % p

	return R

def check_residue(y_2, p):
    residue = (y_2**((p-1)/2)) % p
    return residue == 1

def short_weiertrass(a, b, x, p):
    y_2 = (x*x*x + a*x + b) % p
    return tonelli_shanks(p, y_2)

def twisted_edwards(a, b, x, p):
    y_2 = ((1-a*x*x)/(1-b*x*x))
    fract = find_frac(y_2)
    denom_inv = mod_inverse(fract.denominator, p)
    y_2 = (fract.numerator * denom_inv) % p
    return tonelli_shanks(p, y_2)

def montgomery(a, b, x, p):
    y_2 = (x*x*x + a*x*x + x)/b
    fract = find_frac(y_2)
    denom_inv = mod_inverse(fract.denominator, p)
    y_2 = (fract.numerator * denom_inv) % p
    return tonelli_shanks(p, y_2)

def check_curve(type_curve, a, b, x, p):
    if type_curve == 1:
        return short_weiertrass(a, b, x, p)
    elif type_curve == 2:
        return twisted_edwards(a, b, x, p)
    elif type_curve == 3:
        return montgomery(a, b, x, p)
    else:
        return None
