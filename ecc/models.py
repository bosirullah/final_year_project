# ecc/models.py
from django.db import models

class ECCInput(models.Model):
    option_choices = [
        ('order_of_curve', 'Order of Curve'),
        ('order_of_point', 'Order of Point'),
        ('find_y', 'Find Y'),
        ('generator_point', 'Generator Point'),
    ]

    curve_options = [
        (1, 'Short Weierstrass'),
        (2, 'Twisted Edwards'),
        (3, 'Montgomery'),
    ]

    option = models.CharField(max_length=20, choices=option_choices)
    a = models.PositiveIntegerField()
    b = models.PositiveIntegerField()
    p = models.PositiveIntegerField()
    x = models.PositiveBigIntegerField()
    y = models.PositiveSmallIntegerField()
    curve_type = models.PositiveSmallIntegerField(max_length=20, choices=curve_options)
    # curve_type = models.PositiveBigIntegerField()
