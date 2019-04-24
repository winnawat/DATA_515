import numpy as np


def isPrime(value):
    is_prime = True
    upper = int(np.ceil(np.sqrt(value)))
    for divisor in range(2, upper+1):
        if value % divisor == 0:
            is_prime = False
            break
    return is_prime

def subPrime(value):
    primelist = []
    for value in range(2, value+1):
        if isPrime(value):
            primelist.append(value)
            pass
    return primelist
