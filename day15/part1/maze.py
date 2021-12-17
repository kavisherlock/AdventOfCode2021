f = open("../input", "r")

contents = f.readlines()

grid = []
for line in contents:
  grid.append(map(lambda x: int(x), line.strip()))

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

print(grid[n_cols - 1][n_rows - 1])
