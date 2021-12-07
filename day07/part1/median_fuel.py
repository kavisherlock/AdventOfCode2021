f = open("../input", "r")

contents = f.readlines()
crabs = contents[0].split(',')
crabs = list(map(lambda x: int(x.strip()), crabs))
crabs.sort()
median = crabs[len(crabs) / 2]

median_fuel = sum(map(lambda x: abs(x-median), crabs))

print(median, median_fuel)

