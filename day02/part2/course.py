f = open("../input", "r")

contents = f.readlines()

horizontal = 0
depth = 0
aim = 0
for step in contents:
  if len(step.strip()) == 0: continue
  step_info = step.split(' ')
  direction = step_info[0]
  value = int(step_info[1])
  if direction == 'forward':
    horizontal += value
    depth += value * aim
  if direction == 'up':
    aim -= value
  if direction == 'down':
    aim += value

print(horizontal * depth)
