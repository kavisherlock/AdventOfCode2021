f = open("../input", "r")
contents = f.readlines()

heightmap = []
basin_counted = []
edge = '9' * (len(contents[0]) + 1)
heightmap.append(edge)
basin_counted.append([False] * (len(contents[0]) + 1))
for line in contents:
  heightmap.append('9' + line.strip() + '9')
  basin_counted.append([False] * (len(contents[0]) + 1))
heightmap.append(edge)
basin_counted.append([False] * (len(contents[0]) + 1))

def find_basin_length(i, j):
  cur = int(heightmap[i][j])
  if cur == 9 or basin_counted[i][j]:
    return 0
  basin_counted[i][j] = True
  up = int(heightmap[i - 1][j])
  down = int(heightmap[i + 1][j])
  left = int(heightmap[i][j - 1])
  right = int(heightmap[i][j + 1])

  if cur >= up and cur >= down and cur >= left and cur >= right:
    return 1

  basin_size = 0
  if cur < up:
    basin_size += find_basin_length(i - 1, j)
  if cur < down:
    basin_size += find_basin_length(i + 1, j)
  if cur < left:
    basin_size += find_basin_length(i, j - 1)
  if cur < right:
    basin_size += find_basin_length(i, j + 1)
  
  return 1 + basin_size

basin_sizes = []
for i in range(1, len(heightmap) - 1):
  for j in range(1, len(heightmap[0]) - 1):
    cur = int(heightmap[i][j])
    up = int(heightmap[i - 1][j])
    down = int(heightmap[i + 1][j])
    left = int(heightmap[i][j - 1])
    right = int(heightmap[i][j + 1])

    if cur < up and cur < down and cur < left and cur < right:
      basin_sizes.append(find_basin_length(i, j))

sorted_basin_sizes = sorted(basin_sizes)
print(sorted_basin_sizes)
print(sorted_basin_sizes[-1] * sorted_basin_sizes[-2] * sorted_basin_sizes[-3])