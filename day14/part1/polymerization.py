from collections import Counter

f = open("../input", "r")

contents = f.readlines()
polymer = contents[0].strip()

insertions = {}
for i in range(2, len(contents)):
  rule = contents[i].strip().split(' -> ')
  insertions[rule[0]] = rule[1]

for step in range(0, 10):
  next_polymer = ''
  for i in range(0, len(polymer) - 1):
    pair = polymer[i] + polymer[i + 1]
    next_polymer += polymer[i] + insertions[pair]
  next_polymer += polymer[-1]
  polymer = next_polymer

counts = Counter(polymer).values()
print(max(counts) - min(counts))
