from day04 import Grid

example_map = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_diagram_example():
    out_map = """
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.""".strip()

    grid = Grid.from_map(example_map)
    # ad hoc solution to mark the x's
    working_grid = [[c for c in row] for row in grid.grid]

    # mark the accessible spaces
    for i in range(grid.n_rows):
        for j in range(grid.n_cols):
            if i == 0 and j == 7:
                print("inside: ", grid.n_adjacent_rolls(i, j))

            if grid.grid[i][j] == "@" and grid.n_adjacent_rolls(i, j) < 4:
                working_grid[i][j] = "x"

    working_map = "\n".join(["".join(row) for row in working_grid])
    assert working_map == out_map

    assert grid.n_accessible_rolls() == 13


def test_remove():
    grid = Grid.from_map(example_map)
    assert grid.remove_accessible_rolls() == 43
