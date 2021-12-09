f = open("../input", "r")
contents = f.readlines()

heightmap = []
edge = '9' * (len(contents[0]) + 1)
heightmap.append(edge)
for line in contents:
  heightmap.append('9' + line.strip() + '9')
heightmap.append(edge)

low_point_total = 0
for i in range(1, len(heightmap) - 1):
  for j in range(1, len(heightmap[0]) - 1):
    cur = int(heightmap[i][j])
    up = int(heightmap[i - 1][j])
    down = int(heightmap[i + 1][j])
    left = int(heightmap[i][j - 1])
    right = int(heightmap[i][j + 1])

    if cur < up and cur < down and cur < left and cur < right:
      low_point_total += cur + 1

print(low_point_total)
