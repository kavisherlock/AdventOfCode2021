f = open("../input", "r")
contents = f.readlines()

signals = []
outputs = []

for line in contents:
  entry = line.strip().split(' | ')
  signals.append(entry[0])
  outputs.append(entry[1])

n_easy_digits = 0
for sequence in outputs: 
  digits = sequence.split(' ')
  n_easy_digits += len(filter(lambda d: len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7, digits))

print(n_easy_digits)

