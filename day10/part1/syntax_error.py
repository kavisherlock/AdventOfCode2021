f = open("../input", "r")
contents = f.readlines()

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

total_syntax_error = 0
for line in contents:
  stack = []
  for char in line.strip():
    if char in openers:
      stack.append(char)
    else:
      last_opener = stack.pop()
      if closers[openers.index(last_opener)] != char:
        total_syntax_error += points[char]
        break

print(total_syntax_error)
