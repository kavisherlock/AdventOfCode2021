import math

testinput = 'x=20..30, y=-10..-5'
input = 'x=235..259, y=-118..-62'

target_area = input.split(', ')
target_x = map(int, target_area[0][2:].split('..'))
target_y = map(int, target_area[1][2:].split('..'))
# print(target_x, target_y)

def move_one_step(x, y, v_x, v_y):
  x += v_x
  y += v_y
  v_x = 0 if v_x == 0 else (v_x - 1 if v_x > 0 else v_x + 1)
  v_y -= 1
  return x, y, v_x, v_y

def does_it_reach_target(v_x, v_y, min_x, max_x, min_y, max_y):
  prev_x = 0
  prev_y = 0
  x = 0
  y = 0
  n_steps = 1
  while x <= max_x and y >= min_y:
    prev_x = x
    prev_y = y
    x, y, v_x, v_y = move_one_step(x, y, v_x, v_y)
    n_steps += 1
  return prev_x >= min_x and prev_y <= max_y

min_v_x = int(math.ceil((-1 + (1 + 4 * 2 * target_x[0]) ** 0.5) / (2))) # any slower won't reach the target. This is solution to quadratic equation n(n+1)/2 = x
max_v_x = target_x[1] # Directly throw at the right edge of target

min_v_y = target_y[0] # Directly throw at bottom edge of target
max_v_y = target_y[0] * -1 - 1 # And faster would overshoot once it comes back down

n_vels = 0
for i in range(min_v_x, max_v_x + 1):
  for j in range(min_v_y, max_v_y + 1):
    if does_it_reach_target(i, j, target_x[0], target_x[1], target_y[0], target_y[1]):
      n_vels += 1
print(n_vels)
