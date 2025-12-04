from typing import Self


class OffGrid:
    pass


class Grid:
    roll = "@"
    map_values = ("@", ".")

    def __init__(self, grid: list[list[str]], max_blocks: int = 3):
        self.grid = grid
        self.max_blocks = max_blocks

        self._validate_grid(self.grid)

        self.n_rows = len(grid)
        self.n_cols = len(grid[0])

    @classmethod
    def from_map(cls, map_: str) -> Self:
        return cls([[c for c in row.strip()] for row in map_.strip().splitlines()])

    def _validate_grid(self, grid: list[list[str]]) -> bool:
        assert len(set(len(row) for row in grid)) == 1
        assert set(c for row in grid for c in row).issubset(self.map_values)
        return True

    def __getitem__(self, index: tuple[int, int]) -> OffGrid | str:
        assert len(index) == 2
        i, j = index

        if 0 <= i < self.n_rows and 0 <= j < self.n_rows:
            return self.grid[i][j]
        else:
            return OffGrid()

    def __setitem__(self, index: tuple[int, int], value: str):
        assert len(index) == 2
        i, j = index
        self.grid[i][j] = value

    def n_adjacent_rolls(self, i: int, j: int) -> int:
        return sum(
            [
                self[i + di, j + dj] == self.roll
                for di in [-1, 0, 1]
                for dj in [-1, 0, 1]
                if not (di == 0 and dj == 0)
            ]
        )

    def is_accessible_roll(self, i: int, j: int) -> bool:
        return (
            self.grid[i][j] == self.roll
            and self.n_adjacent_rolls(i, j) <= self.max_blocks
        )

    def n_accessible_rolls(self) -> int:
        return sum(
            [
                self.is_accessible_roll(i, j)
                for i in range(self.n_rows)
                for j in range(self.n_cols)
            ]
        )

    def remove_accessible_rolls(self) -> int:
        accessible_rolls = [
            (i, j)
            for i in range(self.n_rows)
            for j in range(self.n_cols)
            if self.is_accessible_roll(i, j)
        ]
        if len(accessible_rolls) == 0:
            return 0
        else:
            for i, j in accessible_rolls:
                self[i, j] = "."

            return len(accessible_rolls) + self.remove_accessible_rolls()


if __name__ == "__main__":
    with open("2025/input04.txt") as f:
        map_ = f.read().strip()

    grid = Grid.from_map(map_)
    print("Part 1: ", grid.n_accessible_rolls())
    print("Part 2: ", grid.remove_accessible_rolls())
