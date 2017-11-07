#! /usr/bin/env python3

anscombe = open('anscombe.txt')

for _ in range(3): next(anscombe) # skip header
data = {}
for n, line in zip(range(1, 12), anscombe):
	observation, x123y1y2y3, x4y4 = line.strip().split(':')
	assert observation.endswith("%i " % n)
	x123, y1, y2, y3 = x123y1y2y3.split()
	x4, y4 =           x4y4.split()
	data[1, n] = (x123, y1)
	data[2, n] = (x123, y2)
	data[3, n] = (x123, y3)
	data[4, n] = (x4, y4)

print("dataset", "observation", "x", "y", sep='\t')
for dataset in range(1, 5):
	for observation in range(1, 12):
		x, y = data[dataset, observation]
		print(dataset, observation, x, y, sep='\t')
