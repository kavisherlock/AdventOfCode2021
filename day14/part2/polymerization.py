from collections import Counter

f = open("../input", "r")

contents = f.readlines()
polymer = contents[0].strip()

pair_counts = {}
for i in range(0, len(polymer) - 1):
  pair = polymer[i] + polymer[i + 1]
  if pair_counts.has_key(pair):
    pair_counts[pair] += 1
  else:
    pair_counts[pair] = 1

insertions = {}
for i in range(2, len(contents)):
  rule = contents[i].strip().split(' -> ')
  insertions[rule[0]] = rule[1]

for step in range(0, 40):
  next_pair_counts = pair_counts.copy()
  for pair in pair_counts.keys():
    pair_count = pair_counts[pair]
    if pair_count == 0: continue

    # Remove the existing pairs
    next_pair_counts[pair] -= pair_count

    # Make the new pairs
    new_element = insertions[pair]
    new_pairs = [pair[0] + new_element, new_element + pair[1]]
    for new_pair in new_pairs:
      if next_pair_counts.has_key(new_pair):
        next_pair_counts[new_pair] += pair_count
      else:
        next_pair_counts[new_pair] = pair_count

  pair_counts = next_pair_counts.copy()

element_counts = {}
for pair in pair_counts.keys():
  for element in pair:
    if element_counts.has_key(element):
      element_counts[element] += pair_counts[pair]
    else:
      element_counts[element] = pair_counts[pair]

# Fix double counting of elements
element_counts[polymer[0]] -= 1
element_counts[polymer[-1]] -= 1
for element in element_counts.keys():
  element_counts[element] /= 2
element_counts[polymer[0]] += 1
element_counts[polymer[-1]] += 1

print(element_counts)
print(max(element_counts.values()) - min(element_counts.values()))