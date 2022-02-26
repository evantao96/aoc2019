import math 

with open('input1.txt', 'r') as f: 
	mass = [int(n.strip()) for n in f.readlines()]

# fuel = [math.floor(m/3)-2 for m in mass]
# print(sum(fuel))

def getFuel(n): 
	sumFuel = 0
	while(True):
		n = math.floor(n/3)-2
		if(n < 0):
			break
		sumFuel += n
	return(sumFuel)

fuel = [getFuel(m) for m in mass]
print(sum(fuel))
