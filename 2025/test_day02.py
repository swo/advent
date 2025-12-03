from day02 import invalid_in_ranges, is_valid1, is_valid2, run_lengths

example_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_example1():
    """Part 1 example"""
    ids = invalid_in_ranges(example_ranges, is_valid1)
    assert ids == [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
    assert sum(ids) == 1227775554


def test_invalid2():
    assert is_valid2(12)

    for x in [12341234, 123123123, 1212121212, 1111111]:
        assert not is_valid2(x)


def test_example2():
    ids = invalid_in_ranges(example_ranges, is_valid2)
    assert ids == [
        11,
        22,
        99,
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121,
    ]
    assert sum(ids) == 4174379265


def test_run_lengths():
    assert run_lengths(2) == [1]
    assert set(run_lengths(12)) == {1, 2, 3, 4, 6}
