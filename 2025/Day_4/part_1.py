def forklifting(filepath: str) -> int:
    grid: list[list[str]]
    with open(filepath, "r", encoding="utf-8") as file:
        grid = [list(line) for line in file.read().strip().splitlines()]

    ROWS = len(grid)
    COLUMNS = len(grid[0])
    NEIGHBORS = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

    forkliftable_rolls: int = 0

    for current_row, row in enumerate(grid):
        for current_column, character in enumerate(row):
            neighbouring_rolls: int = 0
            if character == "@":
                for (row_offset, col_offset) in NEIGHBORS:
                    neighbor_row = current_row + row_offset
                    neighbor_col = current_column + col_offset
                    if 0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLUMNS and grid[neighbor_row][neighbor_col] == "@":
                        neighbouring_rolls += 1
                if neighbouring_rolls < 4:
                    forkliftable_rolls += 1
    return forkliftable_rolls
    
print(forklifting("./2025/Day_4/input"))