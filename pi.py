import math
from numba import jit


@jit(nopython=True)
def fac(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def piByEuler(n):
    sum = 0
    for i in range(n):
        sum += 2**i * fac(i)**2 / fac(2*i + 1)
    return sum*2
    # problema: retorna cosas muy raras en numeros elevados por el factorial


def piEuler2(n):
    sum = 0
    for i in range(n + 1):
        sum += 2**i * math.factorial(i)**2 / math.factorial(2*i + 1)
    return sum*2


def piByWillis(n):
    product = 1
    for i in range(1, n + 1):
        product *= (2*i / 2*i - 1) * (2*i / 2*i + 1)
    return 2*product


@jit(nopython=True)
def piByBasilea(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i**2
    return math.sqrt(sum*6)
