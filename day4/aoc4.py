with open('input4.txt', 'r') as f:
	contents = f.readline().split('-')

def has_double_digit(num):
	pairs = list(zip(str(num), str(num)[1:]))
	count_pairs = {}
	for digit_1, digit_2 in pairs: 
		if digit_1 == digit_2:
			if (digit_1, digit_2) in count_pairs:
				count_pairs[(digit_1, digit_2)] += 1
			else:
				count_pairs[(digit_1, digit_2)] = 1
	return 1 in count_pairs.values()

def is_increasing(num):
	pairs = list(zip(str(num), str(num)[1:]))
	for digit_1, digit_2 in pairs: 
		if digit_2 < digit_1:
			return False
	return True

start = int(contents[0])
end = int(contents[1])
count = 0
for i in range(start, end+1):
	if has_double_digit(i) and is_increasing(i):
		count += 1
print(count)