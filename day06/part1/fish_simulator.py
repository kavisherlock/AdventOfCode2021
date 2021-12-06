f = open("../input", "r")

contents = f.readlines()
fishes = list(map(lambda f: int(f.strip()), contents[0].split(',')))
N_DAYS = 80

for i in range(N_DAYS):
  # print(fishes)
  n_new_fish = 0
  next_fishes = []
  for fish in fishes:
    next_fish = fish - 1
    if next_fish == -1:
      n_new_fish += 1
      next_fishes.append(6)
    else:
      next_fishes.append(next_fish)
  for j in range(n_new_fish):
    next_fishes.append(8)
  fishes = next_fishes

print(len(fishes))