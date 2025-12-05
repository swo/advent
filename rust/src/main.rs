pub mod day02;

fn main() {
    let ranges = std::fs::read_to_string("../2025/input02.txt").unwrap();
    println!("Part 1: {}", day02::part1(&ranges));
    println!("Part 2: {}", day02::part2(&ranges));
}
