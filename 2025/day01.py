class Dial:
    def __init__(self, x0=50, nx=100):
        """
        Args:
            x0 (int, optional): Initial dial position. Defaults to 50.
            nx (int, optional): Number of dial positions. Defaults to 100.
        """
        self.x = x0
        self.nx = nx
        self.n_zero_crosses = 0
        self.n_zero_stops = 0

    def run(self, program: str):
        """Run a "program" of newline-separated commands"""
        for command in program.strip().splitlines():
            self._rotate(command)

        return self

    def _rotate(self, command: str):
        """Rotate the dial according to a command like "L68" """
        # validate the command
        assert isinstance(command, str)
        assert command[0] in ["L", "R"]
        assert len(command) >= 2
        assert self.is_integer_castable(command[1:])

        # parse the command
        sign = -1 if command[0] == "L" else 1
        size = int(command[1:])

        # do the number of individual clicks required
        for _ in range(size):
            self._click(sign)

        if self.x == 0:
            self.n_zero_stops += 1

    def _click(self, sign: int):
        assert sign in [1, -1]
        self.x = (self.x + sign) % self.nx

        # check if we landed on zero
        if self.x == 0:
            self.n_zero_crosses += 1

    @staticmethod
    def is_integer_castable(s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False


# check the example program
example_program = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

example = Dial().run(example_program)
assert example.n_zero_stops == 3
assert example.n_zero_crosses == 6

# run my puzzle
with open("2025/input01.txt") as f:
    program = f.read()

puzzle = Dial().run(program)
print("No. of zero stops: ", puzzle.n_zero_stops)
print("No. of zero crosses: ", puzzle.n_zero_crosses)
