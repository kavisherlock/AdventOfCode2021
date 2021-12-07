f = open("../input", "r")

contents = f.readlines()
crabs = contents[0].split(',')
crabs = list(map(lambda x: int(x.strip()), crabs))
crabs.sort()
mean = int(sum(crabs) / len(crabs))

mean_fuel = sum(map(lambda x: abs(x-mean) * (abs(x-mean) + 1) / 2, crabs))

print(mean, mean_fuel)

