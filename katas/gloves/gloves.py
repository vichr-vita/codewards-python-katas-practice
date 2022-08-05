"""
Winter is coming, you must prepare your ski holidays.
The objective of this kata is to
determine the number of pair of gloves
you can constitute from the gloves you have in your drawer.

Given an array describing the color of each glove,
return the number of pairs you can constitute,
assuming that only gloves of the same color can form pairs.

Examples:
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)
"""

from typing import List


def nearest_even_floor(n: int) -> int:
    return n if n % 2 == 0 else n - 1


def solution(gloves: List[str]) -> int:
    """
    create a dict where keys are the gloves colors D
    run through the array and increment each key value for matching color
    run through the values of the dict and take nearest (down) even value and divide by two
    accumulate the quotients -> this is the result
    """
    colors = {glove: 0 for glove in gloves}
    for glove in gloves:
        colors[glove] += 1

    pair_count = 0
    for glove_count in colors.values():
        pair_count += (nearest_even_floor(glove_count)/2)

    return int(pair_count)
