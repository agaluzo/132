from math import pi, tan


def polysum(n, s):
    area = 0.25 * n * s**2 / tan(pi/n)
    square_length = (n*s)**2
    return area + square_length
print(polysum(56, 86))
print(polysum(22, 36))
print(polysum(66, 66))
print(polysum(22, 28))
print(polysum(1, 98))
print(polysum(19, 72))
