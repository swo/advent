import functools
import itertools
from typing import Callable


def invalid_in_ranges(ranges: str, is_valid_fun: Callable[[int], bool]) -> list[int]:
    return list(itertools.filterfalse(is_valid_fun, enumerate_from_ranges(ranges)))


def enumerate_from_ranges(ranges: str):
    for start, end in parse_id_ranges(ranges):
        for x in range(start, end + 1):
            yield x


def parse_id_ranges(ranges: str) -> list[tuple[int, int]]:
    return [parse_id_range(range_) for range_ in ranges.split(",")]


def parse_id_range(range_: str) -> tuple[int, int]:
    values = range_.split("-")
    assert len(values) == 2
    return (int(values[0]), int(values[1]))


def is_valid1(x: int) -> bool:
    """Part 1 valid IDs: not a two-part repeat"""
    s = str(x)
    if len(s) % 2 == 0:
        # number is of even length
        # look at the half-length segments; if they are the same, that's invalid
        hl = len(s) // 2
        return s[:hl] != s[hl:]
    else:
        # odd-length numbers are always valid
        return True


def is_valid2(x: int) -> bool:
    """Part 2 valid IDs: there is no repeated substring"""
    s = str(x)

    # all length-1 IDs are valid
    if len(s) == 1:
        return True

    # an ID is invalid if:
    # - for some run of length N
    # - the x/N substrings of length N are identical
    for n in run_lengths(len(s)):
        if len(set(itertools.batched(s, n, strict=True))) == 1:
            return False

    return True


@functools.cache
def run_lengths(x: int) -> list[int]:
    """
    Like the divisors, except the length of possibly-repeated substrings

    Eg 2 -> [1], 4 -> [1, 2], 12 -> [1, 2, 3, 4, 6]
    """
    if x <= 1:
        raise ValueError
    else:
        return [i for i in range(1, x // 2 + 1) if x % i == 0]


with open("2025/input02.txt") as f:
    ranges = f.read().strip()

print("Part 1: ", sum(invalid_in_ranges(ranges, is_valid1)))
print("Part 2: ", sum(invalid_in_ranges(ranges, is_valid2)))
