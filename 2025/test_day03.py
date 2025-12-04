from day03 import digits_to_int, max_bank_joltage, max_battery_joltage, str_to_digits


def test_str_to_digits():
    assert str_to_digits("1234") == [1, 2, 3, 4]


def test_digit_to_int():
    assert digits_to_int([1, 2, 3, 4]) == 1234


def test_max_battery_joltage2():
    example_pairs = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ]

    for in_, out in example_pairs:
        assert max_battery_joltage(in_, n=2) == out


def test_max_battery_joltage12():
    example_pairs = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ]

    for in_, out in example_pairs:
        assert max_bank_joltage(in_, n=12) == out


def test_max_bank_joltage():
    bank = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111"""

    assert max_bank_joltage(bank, n=2) == 357
