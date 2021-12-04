f = open("../input", "r")

contents = f.readlines()

# Gets the new set of values which match the most/least common bit in the given bit position
def get_new_values(cur_values, bit_pos, get_most_common):
  n_ones = 0
  for n in cur_values:
    if n[bit_pos] == '1': n_ones += 1
  new_values = []
  most_common = '1' if n_ones >= (len(cur_values)) / 2 else '0'
  least_common = '1' if n_ones < (len(cur_values)) / 2 else '0'
  for n in cur_values:
    if get_most_common and n[bit_pos] == most_common:
      new_values.append(n)
    elif not get_most_common and n[bit_pos] == least_common:
      new_values.append(n)
  return new_values

n_bits = len(contents[0].strip())

o2_rating = contents[0:-1]
for i in range(n_bits):
  o2_rating = get_new_values(o2_rating, i, True)
  if len(o2_rating) == 1:
    o2_rating = o2_rating[0].strip()
    break

co2_rating = contents[0:-1]
for i in range(n_bits):
  co2_rating = get_new_values(co2_rating, i, False)
  if len(co2_rating) == 1:
    co2_rating = co2_rating[0].strip()
    break

print(o2_rating, co2_rating)

def bin_to_dec(bin_val):
  dec_val = 0
  for i in range(len(bin_val)):
    dec_val += pow(2, i) * int(bin_val[len(bin_val) - i - 1])
  return dec_val

print(bin_to_dec(o2_rating) * bin_to_dec(co2_rating))
