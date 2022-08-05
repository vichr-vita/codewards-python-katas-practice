

from typing import Any, List


def rotate(data: List[Any], n: int) -> List[Any]:
    return [data[(i - n % len(data))] for i, _ in enumerate(data)]
