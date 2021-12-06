f = open("../input", "r")

contents = f.readlines()

DIMENSION = 1000

ocean_floor = []
for i in range(DIMENSION):
  ocean_floor.append([0] * DIMENSION)

for pipe in contents:
  if len(pipe.strip()) == 0: continue
  pipe_ends = pipe.strip().split(' -> ')
  end1 = pipe_ends[0].split(',')
  x1 = int(end1[0])
  y1 = int(end1[1])
  end2 = pipe_ends[1].split(',')
  x2 = int(end2[0])
  y2 = int(end2[1])

  x_increment = 1 if x1 < x2 else (0 if x1 == x2 else -1)
  y_increment = 1 if y1 < y2 else (0 if y1 == y2 else -1)
  distance = abs(x1 - x2) if x_increment != 0 else abs(y1 - y2)
  for i in range(distance + 1):
     ocean_floor[y1 + (y_increment * i)][x1 + (x_increment * i)] += 1

n_overlaps = 0
for row in ocean_floor:
  for point in row:
    if point > 1:
      n_overlaps += 1
print(n_overlaps)
