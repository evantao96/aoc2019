import numpy as np

with open('input3.txt', 'r') as f: 
	wire1 = [(n[0], int(n[1:])) for n in f.readline().strip().split(',')]
	wire2 = [(n[0], int(n[1:])) for n in f.readline().strip().split(',')]

direction = {'R':np.array([1,0]), 'U':np.array([0,1]), 'D':np.array([0,-1]), 'L':np.array([-1,0])}

coords = {}
start = np.array([0, 0])
steps = 0
for d, u in wire1:
	for i in range(u):
		start += direction[d]
		steps += 1
		coords[tuple(start)] = [1, steps]

start = np.array([0, 0])
steps = 0
for d, u in wire2:
	for i in range(u):
		start += direction[d]
		steps += 1
		if (tuple(start) in coords):
			coords[tuple(start)][0] += 1
			coords[tuple(start)][1] += steps

intersect = []
# for coord, count in coords.items():
# 	if count == 2:
# 		intersect += [abs(coord[0])+abs(coord[1])]

for coord, [count, steps] in coords.items():
	if count == 2:
		intersect += [steps]

print(min(intersect))