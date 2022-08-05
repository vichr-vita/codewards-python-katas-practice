
import math


def high_and_low(numbers: str) -> str:
    maximum = -math.inf
    minimum = math.inf
    for n in (int(m) for m in numbers.split(' ')):
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    return str(maximum) + ' ' + str(minimum)
