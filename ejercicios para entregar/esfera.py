from math import *

radio = ""


def volumen(radio):
    return 4/3 * pi * (radio ** 3)

print(volumen(int(input("ingrese el radio: "))))