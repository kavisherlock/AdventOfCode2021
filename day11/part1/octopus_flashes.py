f = open("../input", "r")
contents = f.readlines()

n_flashes = 0
octopus_grid = []
for line in contents:
  octopus_grid.append(list(map(lambda c: int(c), line.strip())))

def increment_grid(grid):
  for row in grid:
    for i in range(len(row)):
      row[i] += 1

def flashes_remaining(grid):
  for row in grid:
    for octopus in row:
      if octopus > 9:
        return True
  return False

def one_flash_round(grid):
  n_flashes = 0
  for r in range(len(grid)):
    for o in range(len(grid[0])):
      if grid[r][o] > 9:
        n_flashes += 1
        grid[r][o] = -100
        if o - 1 >= 0: grid[r][o - 1] += 1
        if o + 1 <= len(grid) - 1: grid[r][o + 1] += 1
        if r - 1 >= 0:
          grid[r - 1][o] += 1
          if o - 1 >= 0: grid[r - 1][o - 1] += 1
          if o + 1 <= len(grid) - 1: grid[r - 1][o + 1] += 1
        if r + 1 <= len(grid) - 1:
          grid[r + 1][o] += 1
          if o - 1 >= 0: grid[r + 1][o - 1] += 1
          if o + 1 <= len(grid) - 1: grid[r + 1][o + 1] += 1
  return n_flashes

def reset_flashed_octupuses(grid):
  for row in grid:
    for i in range(len(row)):
      if row[i] < 0:
        row[i] = 0

def print_grid(grid):
  for row in grid:
    print(row)

print_grid(octopus_grid)
for i in range(100):
  increment_grid(octopus_grid)
  while flashes_remaining(octopus_grid):
    n_flashes += one_flash_round(octopus_grid)
  reset_flashed_octupuses(octopus_grid)
print(n_flashes)
print_grid(octopus_grid)
