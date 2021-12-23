testinput = 'x=20..30, y=-10..-5'
input = 'x=235..259, y=-118..-62'

target_area = input.split(', ')
target_x = map(int, target_area[0][2:].split('..'))
target_y = map(int, target_area[1][2:].split('..'))

init_y_vel = target_y[0] * -1 - 1
highest_point = init_y_vel * (init_y_vel + 1) / 2
print(highest_point)
