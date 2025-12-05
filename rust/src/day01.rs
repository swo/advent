use std::cmp::Ordering;

pub struct Dial {
    position: isize,
    n_positions: isize,
    n_zero_cross: isize,
    n_zero_stop: isize,
}

#[derive(Copy, Clone)]
pub enum Direction {
    L,
    R,
}

impl Dial {
    pub fn run_program(&mut self, program: String) {
        for line in program.lines() {
            self.run_line(line)
        }
    }

    fn run_line(&mut self, line: &str) {
        let direction = match &line[0..1] {
            "L" => Direction::L,
            "R" => Direction::R,
            _ => panic!("bad value"),
        };

        let amount = line[1..]
            .parse::<isize>()
            .unwrap_or_else(|_| panic!("non-integer value: '{}'", &line[1..]));
        self.rotate(direction, amount);
    }

    fn rotate(&mut self, direction: Direction, amount: isize) {
        match 0.cmp(&amount) {
            Ordering::Greater => panic!("negative rotation: '{}'", amount),
            Ordering::Equal => {}
            Ordering::Less => {
                for _ in 1..=amount {
                    self.click(direction)
                }
                if self.position == 0 {
                    self.n_zero_stop += 1;
                }
            }
        }
    }

    fn click(&mut self, direction: Direction) {
        self.position = (self.position
            + match direction {
                Direction::L => -1,
                Direction::R => 1,
            })
        .rem_euclid(self.n_positions);

        if self.position == 0 {
            self.n_zero_cross += 1
        }

        if (self.position < 0) || (self.position >= self.n_positions) {
            panic!("bad position: {}", self.position)
        }
    }
}

pub fn new_dial() -> Dial {
    Dial {
        position: 50,
        n_positions: 100,
        n_zero_cross: 0,
        n_zero_stop: 0,
    }
}

pub fn run() {
    let program = std::fs::read_to_string("../2025/input01.txt").unwrap();
    let mut dial = new_dial();
    dial.run_program(program);
    println!("Part 1: {}", dial.n_zero_stop);
    println!("Part 2: {}", dial.n_zero_cross);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let program = indoc::indoc! {"
            L68
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82
        "}
        .to_string();

        let mut dial = new_dial();
        dial.run_program(program);
        assert_eq!(dial.n_zero_stop, 3);
        assert_eq!(dial.n_zero_cross, 6);
    }
}
