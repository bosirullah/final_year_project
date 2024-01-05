from sympy import legendre,isprime

def check_prime(m):
    while not isprime(m):
        m = m.nextprime()
    return m

def find_points(a, b, m):
    no_of_points = 0
    
    for x in range(m):
        xx = (x**3 + a*x + b) % m

        if xx == 0:
            no_of_points += 1

        legendre_symbol = legendre(xx, m)
        if legendre_symbol == 1:
            temp1 = (m + 1) // 4
            y = pow(xx, temp1, m)
            no_of_points += 1

            if y > m // 2:
                y = m - y
                no_of_points += 1

    no_of_points += 1  # Including the point at infinity
    return no_of_points

# if _name_ == "_main_":
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     m = int(input("Enter the prime field: "))

#     m = check_prime(m)
#     print(f"Prime field is: {m}")

#     order = find_points(a, b, m)
#     print(f"\nThe Order of the Curve is: {order}")