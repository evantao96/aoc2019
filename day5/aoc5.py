with open('input5.txt', 'r') as f: 
	orig = [int(n) for n in f.readline().split(',')]
 
for noun in range(100): 
	for verb in range(100):
		nums = orig.copy()

		nums[1] = noun
		nums[2] = verb

		for i in range(0, len(nums), 4): 
			op = nums[i]
			if (op == 1):
				nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
			elif (op == 2):
				nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
			#elif (op == 3): save input at address of parameter
			#elif (op == 4): output at address of parameter


		if (nums[0] == 19690720): 
			print(100*noun+verb)

