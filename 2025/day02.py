def invalid_in_ranges(ranges: str):
    return [x for x in enumerate_from_ranges(ranges) if not is_valid(x)]


def enumerate_from_ranges(ranges: str):
    for start, end in parse_id_ranges(ranges):
        for x in range(start, end + 1):
            yield x


def parse_id_ranges(ranges: str) -> list[tuple[int, int]]:
    return [parse_id_range1(range_) for range_ in ranges.split(",")]


def parse_id_range1(range_: str) -> tuple[int, int]:
    values = range_.split("-")
    assert len(values) == 2
    return (int(values[0]), int(values[1]))


def is_valid(x: int) -> bool:
    s = str(x)
    if len(s) % 2 == 0:
        # number is of even length
        # look at the half-length segments; if they are the same, that's invalid
        hl = len(s) // 2
        return s[:hl] != s[hl:]
    else:
        # odd-length numbers are always valid
        return True


# check the example
example_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
assert invalid_in_ranges(example_ranges) == [
    11,
    22,
    99,
    1010,
    1188511885,
    222222,
    446446,
    38593859,
]

assert sum(invalid_in_ranges(example_ranges)) == 1227775554

with open("2025/input02.txt") as f:
    ranges = f.read().strip()

print(sum(invalid_in_ranges(ranges)))
