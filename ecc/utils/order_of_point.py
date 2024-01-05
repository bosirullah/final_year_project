from sympy import isprime

# def add_point(a, b, p, xp, yp, xq, yq):
#     # ... (Implementation of point addition)
#     pass

# def double_point(a, b, p, xp, yp):
#     # ... (Implementation of point doubling)
#     pass

def find_order(a, b, p, xp, yp):
    xq, yq, xr, yr, c = xp, yp, 0, 0, 1  # Initialize variables

    # double_point(a, b, p, xq, yq)
    if xr == yr == 0:
        return 2

    c += 1
    xq, yq = xr, yr

    while True:
        c += 1
        if xp == xq:
            return c
        else:
            # add_point(a, b, p, xp, yp, xq, yq)
            xq, yq = xr, yr

# # Main function
# def main():
#     # Initialize variables
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     p = int(input("Enter the prime field: "))
#     xp = int(input("Enter the x-coordinate of the point: "))
#     yp = int(input("Enter the y-coordinate of the point: "))

#     # Check if p is prime
#     while not isprime(p):
#         p += 1

#     # Find the order of the point
#     order = find_order(a, b, p, xp, yp)
#     print(f"\nOrder is: {order}")

# if _name_ == "_main_":
#     main()