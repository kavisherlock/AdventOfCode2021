f = open("../input", "r")

contents = f.readlines()
fishes = list(map(lambda f: int(f.strip()), contents[0].split(',')))
N_DAYS = 256

fish_counts = [0] * 9
for fish in fishes:
  fish_counts[fish] += 1

print(fish_counts)
for i in range(N_DAYS):
  n_zero_fish = fish_counts[0]
  for n in range(len(fish_counts) - 1):
    fish_counts[n] = fish_counts[n + 1]
  fish_counts[6] += n_zero_fish
  fish_counts[8] = n_zero_fish

total_fish = 0
for c in fish_counts:
  total_fish += c
print(fish_counts)
print(total_fish)
