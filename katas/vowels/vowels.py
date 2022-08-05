

from typing import List


def solution(text: str) -> List[int]:
    VOVELS = {'a', 'e', 'i', 'o', 'u', 'y'}
    indices = []
    for i, ch in enumerate(text.lower()):
        if ch in VOVELS:
            indices.append(i + 1)
    return indices
