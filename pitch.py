from math import pow

def inverse(n, minor):
    n -= minor
    weird = pow(2, 1/12)
    result = 440 * pow(weird, n)
    return round(result, 2)