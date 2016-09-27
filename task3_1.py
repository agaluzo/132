from math import pi, tan


def polysum(n, s):
    def area():
        return 0.25 * n * s**2 / tan(pi/n)

    def square_perimeter():
        return (n*s)**2

    return area() + square_perimeter()
print(polysum(56, 86))
print(polysum(22, 36))
print(polysum(66, 66))
print(polysum(22, 28))
print(polysum(1, 98))
print(polysum(19, 72))
