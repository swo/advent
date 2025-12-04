def max_battery_joltage(battery: str, n: int) -> int:
    digits = str_to_digits(battery)
    return digits_to_int(_f(digits, n))


def _f(digits: list[int], n: int) -> list[int]:
    assert n <= len(digits)

    if len(digits) == n:
        return digits
    elif n == 1:
        return [max(digits)]
    else:
        # get the next highest digit from the next not-N-to-last digits
        d = max(digits[: (-n + 1)])
        i = digits.index(d)
        # return this digit, plus the result that comes from looking at the remaining digits
        return [d] + _f(digits[(i + 1) :], n - 1)


def str_to_digits(s: str) -> list[int]:
    return [int(y) for y in s]


def digits_to_int(digits: list[int]) -> int:
    return sum(d * 10**i for i, d in enumerate(reversed(digits)))


def max_bank_joltage(bank: str, n: int) -> int:
    batteries = [line.strip() for line in bank.strip().splitlines()]
    joltages = [max_battery_joltage(x, n) for x in batteries]
    return sum(joltages)


if __name__ == "__main__":
    with open("2025/input03.txt") as f:
        bank = f.read()

    print("Part 1: ", max_bank_joltage(bank, n=2))
    print("Part 2: ", max_bank_joltage(bank, n=12))
