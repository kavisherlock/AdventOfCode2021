f = open("../input", "r")

contents = f.readlines()

increases = 0
prev_depth = int(contents[0])
for depth in contents:
  if not len(depth.strip()):
    continue
  if prev_depth < int(depth):
    increases += 1
  prev_depth = int(depth)

print(increases)
