# ecc/views.py
from sympy import isprime
from django.shortcuts import render
from .forms import ECCInputForm
from .utils.find_y import check_curve as check_curve_y
from .utils.find_generator_point import check_curve as check_curve_generator_point
from .utils.order_of_point import find_order
from .utils.order_of_curve import find_points,check_prime

def ecc_input(request):
    form = ECCInputForm()
    if request.method == 'POST':
        form = ECCInputForm(request.POST)
        if form.is_valid():
            option = form.cleaned_data['option']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            p = form.cleaned_data['p']

            if option == 'find_y':
                x = form.cleaned_data['x']
                type_curve = form.cleaned_data['curve_type']

                # Perform ECC calculations
                y = check_curve_y(type_curve, a, b, x, p)

                if y is None:
                    output_result = "The value isn't a quadratic residue"
                else:
                    output_result = f"The roots are: {y} and {(p - y) % p}"
            elif option == 'generator_point':
                x = form.cleaned_data['x']
                type_curve = form.cleaned_data['curve_type']

                # Perform ECC calculations
                generator_point = check_curve_generator_point(type_curve, a, b, x, p)

                if generator_point is None:
                    output_result = "The value isn't a quadratic residue"
                else:
                    output_result = "Generator Point (x, y): ({}, {})".format(x, generator_point)
            elif option == 'order_of_point':
                xp = form.cleaned_data['x']
                yp = form.cleaned_data['y']

                while not isprime(p):
                    p += 1

                # Find the order of the point
                order = find_order(a, b, p, xp, yp)
                output_result = f"\nOrder is: {order}"
            else : 
                m = check_prime(p)
                order = find_points(a, b, m)
                output_result = f"Prime field is: {m}\nThe Order of the Curve is: {order}"

            return render(request, 'ecc/result.html', {'form': form, 'output_result': output_result})

    return render(request, 'ecc/ecc_input.html', {'form': form})
