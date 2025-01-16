def slide_and_merge(row):
    """Slide the row to the left and merge tiles."""
    new_row = [x for x in row if x != 0]  # Remove all zeros
    for i in range(len(new_row) - 1):  # Merge tiles
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [x for x in new_row if x != 0]  # Remove zeros again after merge
    new_row += [0] * (4 - len(new_row))  # Add zeros to the end to maintain row length
    return new_row

def move_left(grid):
    return [slide_and_merge(row) for row in grid]

def move_right(grid):
    return [slide_and_merge(row[::-1])[::-1] for row in grid]

def move_up(grid):
    transposed = list(map(list, zip(*grid)))  # Transpose the grid
    moved = move_left(transposed)
    return list(map(list, zip(*moved)))  # Transpose back

def move_down(grid):
    transposed = list(map(list, zip(*grid)))  # Transpose the grid
    moved = move_right(transposed)
    return list(map(list, zip(*moved)))  # Transpose back

def apply_move(grid, move):
    if move == 0:
        return move_left(grid)
    elif move == 1:
        return move_up(grid)
    elif move == 2:
        return move_right(grid)
    elif move == 3:
        return move_down(grid)
    else:
        raise ValueError("Invalid move direction")

# Read the input
import sys
input = sys.stdin.read
data = input().split()
grid = [list(map(int, data[i*4:(i+1)*4])) for i in range(4)]
move = int(data[16])

# Apply the move to the grid
result = apply_move(grid, move)

# Print the output
for row in result:
    print(' '.join(map(str, row)))
