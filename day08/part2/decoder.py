f = open("../input", "r")
contents = f.readlines()

signals = []
outputs = []

for line in contents:
  entry = line.strip().split(' | ')
  signals.append(entry[0])
  outputs.append(entry[1])

total = 0
for s in range(len(signals)):
  sequence = signals[s]
  digits = sorted(sequence.split(' '), key=len)
  # print(digits)
  digit_codes = [''] * 10

  # Easy Digits
  digit_codes[1] = digits[0]
  digit_codes[7] = digits[1]
  digit_codes[4] = digits[2]
  digit_codes[8] = digits[9]

  # Segments in 4 but not in 1 (to find 0 later)
  four_minus_one = ''.join((filter(lambda x: x not in digit_codes[1], digit_codes[4])))

  # 6-length Digits
  for i in range(6, 9):
    # 9 must contain 4 entirely
    nine_found = True
    for j in digit_codes[4]:
      if j not in digits[i]:
        nine_found = False
    if nine_found:
      digit_codes[9] = digits[i]

    # 0 must not contain (4 - 1)
    zero_found = not (four_minus_one[0] in digits[i] and four_minus_one[1] in digits[i])
    if zero_found:
      digit_codes[0] = digits[i]
    
    # if not 9 or 0, then 6
    if not zero_found and not nine_found:
      digit_codes[6] = digits[i]

  # 5-length Digits
  for i in range(3, 6):
    # 3 must contain 7 entirely
    three_found = True
    for j in digit_codes[7]:
      if j not in digits[i]:
        three_found = False
        break
    if three_found:
      digit_codes[3] = digits[i]
    else:
      # 6 must contain 5 entirely
      five_found = True
      for j in digits[i]:
        if j not in digit_codes[6]:
          five_found = False
      if five_found:
        digit_codes[5] = digits[i]
      else:
        # if not 3 or 5, then 2
        digit_codes[2] = digits[i]

  digit_map = {}
  for i in range(0, 10):
    digit_map[''.join(sorted(digit_codes[i]))] = i
  # print(digit_codes)
  # print(digit_map)

  # print(outputs[s].split(' '))

  output_total = ''
  for output in outputs[s].split(' '):
    output_total += str(digit_map[''.join(sorted(output))])
  total += int(output_total)

print(total)
