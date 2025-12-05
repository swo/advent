// Does `x` divide into `n` identical substrings?
fn is_valid_n(x: usize, n: usize) -> bool {
    let s = x.to_string();
    // minimium 2 slices, up to each slice being one digit
    assert!(n >= 2);
    assert!(
        n <= s.len(),
        "number of slices {} is more than string int length {}",
        n,
        s.len()
    );

    // not valid if (1) divides evenly by `n` and
    // (2) has repeated slices
    !(s.len() % n == 0 && _has_repeated_slice(&s, n))
}

// Does `x` divide into any number of identical substrings?
fn is_valid_any(x: usize) -> bool {
    let len = x.to_string().len();

    for n in 2..=len {
        if !is_valid_n(x, n) {
            return false;
        }
    }

    true
}

// Does `x` have `n` identical slices?
fn _has_repeated_slice(s: &str, n: usize) -> bool {
    // get slice length
    let sl = s.len() / n;
    // pull out the first slice
    let first_slice = &s[0..sl];
    // compare all the other slices to this one
    for i in 1..n {
        let this_slice = &s[(sl * i)..(sl * (i + 1))];

        if this_slice != first_slice {
            return false;
        }
    }

    true
}

fn parse_range(s: &str) -> std::ops::RangeInclusive<usize> {
    let (start, stop) = s.split_once("-").unwrap();
    let start: usize = start.parse().unwrap();
    let stop: usize = stop.parse().unwrap();

    start..=stop
}

fn filter_ranges(s: &str, predicate: fn(usize) -> bool) -> Vec<usize> {
    s.split(",")
        .flat_map(parse_range)
        .filter(|x: &usize| predicate(*x))
        .collect()
}

fn sum_filter_ranges(s: &str, predicate: fn(usize) -> bool) -> usize {
    filter_ranges(s, predicate).into_iter().sum()
}

pub fn part1(s: &str) -> usize {
    sum_filter_ranges(s, |x| !is_valid_n(x, 2))
}

pub fn part2(s: &str) -> usize {
    sum_filter_ranges(s, |x| !is_valid_any(x))
}

#[cfg(test)]
mod tests {
    use super::*;

    const RANGES: &str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";

    #[test]
    fn test_example_part1() {
        let ids = filter_ranges(RANGES, |x| !is_valid_n(x, 2));
        assert_eq!(
            ids,
            [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
        );
        assert_eq!(sum_filter_ranges(RANGES, |x| !is_valid_n(x, 2)), 1227775554);
    }
    #[test]
    fn test_example2() {
        let ids = filter_ranges(RANGES, |x| !is_valid_any(x));
        assert_eq!(
            ids,
            [
                11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656,
                824824824, 2121212121,
            ]
        );
        assert_eq!(ids.into_iter().sum::<usize>(), 4174379265);
    }

    #[test]
    fn test_is_valid_any() {
        assert!(is_valid_any(12));

        let ids = vec![12341234, 123123123, 1212121212, 1111111];
        for id in ids {
            assert!(!is_valid_any(id), "id {} should be invalid", id);
        }
    }
}
