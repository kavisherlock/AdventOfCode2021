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
    coordinates.append(list(map(lambda x: int(x), line.strip().split(','))))
  else:
    folds.append(line.strip().split(' ')[2])

first_fold = folds[0].split('=')
fold_dir = first_fold[0]
fold_val = int(first_fold[1])
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
print(len(unique_coordinates))
