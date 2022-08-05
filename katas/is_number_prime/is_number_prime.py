"""
Define a function that takes an integer argument
and returns a logical value true or false
depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number
greater than 1 that has no positive divisors other than 1 and itself.
"""
import math


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, math.ceil(math.pow(num, 0.5))+1, 2):
        if num % n == 0:
            return False
        else:
            continue
    return True
