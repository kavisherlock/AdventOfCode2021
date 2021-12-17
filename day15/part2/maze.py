f = open("../input", "r")

contents = f.readlines()

grid = []
for i in range(0, 5):
  for line in contents:
    tile_row = map(lambda x: int(x), line.strip())
    row = []
    for j in range(0, 5):
      row += map(lambda x: (x + i + j if x + i + j < 10 else x + i + j - 9), tile_row)
    grid.append(row)

# for row in grid:
#   print(row)

n_rows = len(grid)
n_cols = len(grid[0])

def get_coordinates_by_distance(d, x, y, max_x, max_y):
  coordinates = []
  for i in range(d + 1):
    if x + (d - i) < max_x and y + i < max_y:
      coordinates.append([x + (d - i), y + i])
    if x - (d - i) >= 0 and y + i < max_y:
      coordinates.append([x - (d - i), y + i])
    if x + (d - i) < max_x and y - i >= 0:
      coordinates.append([x + (d - i), y - i])
    if x - (d - i) >= 0 and y - i >= 0:
      coordinates.append([x - (d - i) + y - i])
  return map(lambda c: map(int, c.split(',')), set(map(lambda c: str(c[0]) + ',' + str(c[1]), coordinates)))

distance_to_goal = n_rows + n_cols - 2

# for row in grid[480:]:
#   print(row[480:])

print(grid[0])
print(sum(grid[0]))

grid[0][0] = 0
for d in range(1, distance_to_goal + 1):
  coordinates = get_coordinates_by_distance(d, 0, 0, n_rows, n_cols)
  for c in coordinates:
    x = c[1]
    y = c[0]
    grid[y][x]
    if x == 0:
      grid[y][x] += grid[y - 1][x]
    elif y == 0:
      grid[y][x] += grid[y][x - 1]
    else:
      grid[y][x] += min(grid[y - 1][x], grid[y][x - 1])

print(grid[0])

# for row in grid[480:]:
#   print(row[480:])

print(grid[n_cols - 1][n_rows - 1])
