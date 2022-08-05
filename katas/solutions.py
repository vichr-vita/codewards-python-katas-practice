from __future__ import annotations
from collections import Counter
import math


def pig_it(text: str) -> str:
    text_l: list = text.split(' ')
    punct: str = ''
    if len(text_l[-1]) == 1:  # assuming punctuation char from the test cases
        punct = ' ' + text_l[-1]
        text_l = text_l[0: -1]
    pig_latinized = [word[1:] + word[0] + 'ay' for word in text_l]
    return ' '.join(pig_latinized) + punct


def move_zeros(lst: list[int]) -> list[int]:
    zeros_indices: set[int] = set([i for i, l in enumerate(lst) if l == 0])
    index_set: set[int] = {i for i in range(0, len(lst))}
    all_other_indices = index_set.difference(zeros_indices)
    return [lst[i] for i in [*sorted(all_other_indices), *zeros_indices]]


def valid_parentheses(string: str) -> bool:
    # TODO
    pass


def keep_in_range(x: int, start: int, end: int) -> int:
    if x <= start:
        return start
    if x >= end:
        return end
    else:
        return x


def rgb(r: int, g: int, b: int) -> str:
    rgb_l = [keep_in_range(x, 0, 255) for x in [r, g, b]]
    return ''.join([str(hex(x))[2:].upper().zfill(2) for x in rgb_l])


def anagrams(word: str, words: list[str]) -> list[str]:
    return [w for wms, w in zip([Counter(w) for w in words], words) if wms == Counter(word)]


def dirReduc(arr: list[str]) -> list[str]:
    pass


def fib_lesseqthan(n: int) -> list[int]:
    """
    return without zero
    """
    if n == 0:
        return [0, 1]
    if n == 1:
        return [0, 1, 1]
    l = [0, 1, 1]
    while l[-1] < n:
        l = [*l, l[-1] + l[-2]]
    if l[-1] > n:
        return l[:-1]
    return l


def productFib(prod):
    fib = fib_lesseqthan(prod)
    for fn, fn_plus in zip(fib, fib[1:]):
        conseq_prod = fn * fn_plus
        if conseq_prod == prod:
            return [fn, fn_plus, True]
        if conseq_prod > prod:
            return [fn, fn_plus, False]
    raise Exception('This should not end here by design.')


def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
    min: int = 999999999
    if len(recipe) > len(available):  # more requirements than avail ingredients
        return 0
    for k in recipe.keys():
        if k not in available.keys():  # ingredient not available
            return 0
    for k, v in available.items():
        # irrelevant ingedient
        if k not in recipe.keys():
            continue
        cakes_with_ingedient = math.floor(v / recipe[k])
        if cakes_with_ingedient < min:
            min = cakes_with_ingedient
    return min
