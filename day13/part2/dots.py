f = open("../input", "r")

contents = f.readlines()

coordinates = []
folds = []

onCoordinates = True
for line in contents:
  if len(line.strip()) == 0:
    onCoordinates = False
    continue
  if onCoordinates:
    coordinates.append(map(lambda x: int(x), line.strip().split(',')))
  else:
    folds.append(line.strip().split(' ')[2])

for fold in folds:
  fold = fold.split('=')
  fold_dir = fold[0]
  fold_val = int(fold[1])
  for c in range(len(coordinates)):
    coordinate = coordinates[c]
    coord_to_change = 0
    if fold_dir == 'y':
      coord_to_change = 1

    if coordinate[coord_to_change] > fold_val:
      distance = coordinate[coord_to_change] - fold_val
      if coord_to_change == 0:
        coordinates[c] = [coordinate[0] - (distance * 2), coordinate[1]]
      else:
        coordinates[c] = [coordinate[0], coordinate[1] - (distance * 2)]

  unique_coordinates = set(map(lambda c: str(c[0]) + ',' + str(c[1]), coordinates))
  coordinates = map(lambda c: map(lambda x: int(x), c.split(',')), unique_coordinates)

# print(coordinates)
max_x = -1
max_y = -1
for coordinate in coordinates:
  if coordinate[0] > max_x:
    max_x = coordinate[0]
  if coordinate[1] > max_y:
    max_y = coordinate[1]

code = []
for j in range(max_y + 1):
  code.append([' '] * (max_x + 1))
for coordinate in coordinates:
  code[coordinate[1]][coordinate[0]] = '#'
for j in range(max_y + 1):
  print(''.join(code[j]))
