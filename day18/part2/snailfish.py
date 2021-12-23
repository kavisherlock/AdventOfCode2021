f = open("../input", "r")
contents = f.readlines()

def string_to_list(snailfish):
  snailfishlist = []
  for i in range(len(snailfish)):
    if snailfish[i] in '[,]':
      snailfishlist.append(snailfish[i])
    elif snailfish[i] == '1' and snailfish[i + 1] not in ',]':
      snailfishlist.append(int(snailfish[i] + snailfish[i + 1]))
    elif snailfish[i - 1] == '1' and snailfish[i] not in ',]':
      continue
    else:
      snailfishlist.append(int(snailfish[i]))
  return snailfishlist

def get_explosion_index(snailfish):
  n_open_pairs = 0
  for i in range(len(snailfish)):
    c = snailfish[i]
    if c == '[':
      n_open_pairs += 1
      if n_open_pairs > 4:
        if snailfish[i + 4] == ']':
          return i
    if c == ']':
      n_open_pairs -= 1
  return -1

def explode_first_pair(snailfish, explosion_index):
  explosion_pair_left_index = explosion_index + 1
  explosion_pair_right_index = explosion_index + 3

  # Snailfish to the left of the exploded pair
  prev_snailfish_index = -1
  for i in range(explosion_pair_left_index):
    if isinstance(snailfish[i], int):
      prev_snailfish_index = i

  # Snailfish to the right of the exploded pair
  next_snailfish_index = -1
  for i in range(explosion_pair_right_index + 1, len(snailfish)):
    if isinstance(snailfish[i], int):
      next_snailfish_index = i
      break

  new_list = []
  if prev_snailfish_index != -1:
    new_list += snailfish[:prev_snailfish_index]
    new_list.append(snailfish[prev_snailfish_index] + snailfish[explosion_pair_left_index])
    new_list += snailfish[prev_snailfish_index + 1:explosion_pair_left_index - 1]
  else:
    new_list += snailfish[:explosion_index]
  
  new_list.append(0)

  if next_snailfish_index != -1:
    new_list += snailfish[explosion_pair_right_index + 2:next_snailfish_index]
    new_list.append(snailfish[next_snailfish_index] + snailfish[explosion_pair_right_index])
    new_list += snailfish[next_snailfish_index + 1:]
  else:
    new_list += snailfish[explosion_pair_right_index + 2:]
  
  return new_list

def get_split_index(snailfish):
  for i in range(len(snailfish)):
    if isinstance(snailfish[i], int) and snailfish[i] >= 10:
      return i
  return -1

def perform_first_split(snailfish, split_index):
  new_list = snailfish[:split_index]
  new_list.append('[')
  new_list.append(snailfish[split_index] / 2)
  new_list.append(',')
  new_list.append(snailfish[split_index] - snailfish[split_index] / 2)
  new_list.append(']')
  new_list += snailfish[split_index + 1:]
  return new_list

def reduce_snailfish(snailfish):
  explosion_index = get_explosion_index(snailfish)
  while explosion_index != -1:
    snailfish = explode_first_pair(snailfish, explosion_index)
    # print(''.join(map(str, snailfish)))
    explosion_index = get_explosion_index(snailfish)
  split_index = get_split_index(snailfish)
  while split_index != -1:
    snailfish = perform_first_split(snailfish, split_index)
    # print(''.join(map(str, snailfish)))
    explosion_index = get_explosion_index(snailfish)
    while explosion_index != -1:
      snailfish = explode_first_pair(snailfish, explosion_index)
      # print(''.join(map(str, snailfish)))
      explosion_index = get_explosion_index(snailfish)
    split_index = get_split_index(snailfish)
  return snailfish

def add_snailfish(s1, s2):
  new_list = []
  new_list.append('[')
  new_list += s1
  new_list.append(',')
  new_list += s2
  new_list.append(']')
  return new_list

def get_magnitude(snailfish_string):
  if len(snailfish_string) == 1:
    return int(snailfish_string[0])
  if len(snailfish_string) == 5:
    return 3 * int(snailfish_string[1]) + 2 * int(snailfish_string[3])

  main_comma_index = -1
  n_open_pairs = 0
  for i in range(1, len(snailfish_string) - 1):
    if snailfish_string[i] == '[':
      n_open_pairs += 1
    if snailfish_string[i] == ']':
      n_open_pairs -= 1

    if snailfish_string[i] == ',' and n_open_pairs == 0:
      main_comma_index = i
      break

  left_pair = snailfish_string[1:main_comma_index]
  right_pair = snailfish_string[main_comma_index + 1:len(snailfish_string) - 1]

  return 3 * get_magnitude(left_pair) + 2 * get_magnitude(right_pair)

largest_magnitude = -1
for i in range(len(contents)):
  for j in range(len(contents)):
    if i != j:
      s1 = string_to_list(contents[i].strip())
      s2 = string_to_list(contents[j].strip())
      sum = reduce_snailfish(add_snailfish(s1, s2))
      magnitude = get_magnitude(''.join(map(str, sum)))
      if magnitude > largest_magnitude:
        largest_magnitude = magnitude

print(largest_magnitude)
