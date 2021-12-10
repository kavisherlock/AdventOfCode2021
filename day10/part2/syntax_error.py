f = open("../input", "r")
contents = f.readlines()

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
points = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

completion_strings = []
for line in contents:
  stack = []
  for char in line.strip():
    if char in openers:
      stack.append(char)
    else:
      last_opener = stack.pop()
      if closers[openers.index(last_opener)] != char:
        stack = []
        break
  if len(stack):
    completion_strings.append(''.join(reversed(map(lambda c: closers[openers.index(c)], stack))))

def get_score(string):
  score = 0
  for c in string:
    score *= 5
    score += points[c]
  return score

scores = sorted(list(map(get_score, completion_strings)))
print(scores[len(scores) / 2])
