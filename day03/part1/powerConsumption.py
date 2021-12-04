f = open("../input", "r")

contents = f.readlines()

n_bits = len(contents[0].strip())
n_ones = [0] * n_bits
print(n_ones)
for n in contents:
  for i in range(len(n.strip())):
    if n[i] == '1': n_ones[i] += 1

print(n_ones)
gamma = ''
epsilon = ''
for n in n_ones:
  if n > (len(contents) - 1) / 2:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'

def bin_to_dec(bin_val):
  dec_val = 0
  for i in range(len(bin_val)):
    dec_val += pow(2, i) * int(bin_val[len(bin_val) - i - 1])
  return dec_val

print(bin_to_dec(gamma) * bin_to_dec(epsilon))
