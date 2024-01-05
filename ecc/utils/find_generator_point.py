# ecc/utils/ecc_operations.py
from fractions import Fraction

# def type_of_curve():
#     print("Enter type of curve:")
#     print("1. Short Weierstrass")
#     print("2. Twisted Edwards")
#     print("3. Montgomery")
#     type_curve = int(input())
#     return type_curve

def find_frac(decimal_value):
    fraction_obj = Fraction(decimal_value).limit_denominator()
    return fraction_obj

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = m, a % m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1

def short_weiertrass(a, b, x, p):
    y_2 = (x * x * x + a * x + b) % p
    return tonelli_shanks(p, y_2)

def twisted_edwards(a, b, x, p):
    y_2 = ((1 - a * x * x) * mod_inverse(1 - b * x * x, p)) % p
    fract = find_frac(y_2)
    denom_inv = mod_inverse(fract.denominator, p)
    y_2 = (fract.numerator * denom_inv) % p
    return tonelli_shanks(p, y_2)

def montgomery(a, b, x, p):
    y_2 = (x * x * x + a * x * x + x) // b
    fract = find_frac(y_2)
    denom_inv = mod_inverse(fract.denominator, p)
    y_2 = (fract.numerator * denom_inv) % p
    return tonelli_shanks(p, y_2)

def check_residue(y_2, p):
    residue = pow(y_2, (p - 1) // 2, p)
    return residue == 1

def tonelli_shanks(p, n):
    if n % p == 0:
        return 0

    if not check_residue(n, p):
        print("This value of n is not a quadratic residue.")
        return None
    else:
        print("This value of n is a quadratic residue.")

    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

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
    R = pow(n, (Q + 1) // 2, p)

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

def check_curve(type_curve, a, b, x, p):
    if type_curve == 1:
        return short_weiertrass(a, b, x, p)
    elif type_curve == 2:
        return twisted_edwards(a, b, x, p)
    elif type_curve == 3:
        return montgomery(a, b, x, p)
    else:
        print("Invalid curve type")
        return None

# generator_point = check_curve()
# if generator_point is None:
#     print("The value isn't a quadratic residue")
# else:
#     print("Generator Point (x, y): ({}, {})".format(x, generator_point))
