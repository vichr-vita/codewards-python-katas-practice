from collections import defaultdict
from typing import List


STRINGS_DICT = {
    0: 'no one likes this',
    1: '{} likes this',
    2: '{} and {} like this',
    3: '{}, {} and {} like this',
}


def solution(names: List[str]) -> str:
    str_template = STRINGS_DICT.get(
        len(names), '{}, {} and {} others like this')
    if len(names) > 3:
        return str_template.format(*names[0:2], len(names) - 2)
    else:
        return str_template.format(*names)
