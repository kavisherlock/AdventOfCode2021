f = open("../input", "r")

contents = f.readlines()

increases = 0
prev_depth = int(contents[0]) + int(contents[1]) + int(contents[2])
for i in range(1, len(contents) - 3):
  depth_window = int(contents[i]) + int(contents[i + 1]) + int(contents[i + 2])
  if prev_depth < depth_window:
    increases += 1
  prev_depth = depth_window

print(increases)
