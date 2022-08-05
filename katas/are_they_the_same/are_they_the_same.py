

from typing import List


def comp(array1: List[int], array2: List[int]) -> bool:
    try:
        return sorted((n**2 for n in array1)) == sorted((n for n in array2))
    except TypeError:
        return False
