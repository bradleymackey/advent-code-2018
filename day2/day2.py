# advent of code day 2
# bradleymackey

# challenge 1
with open('input.txt', 'r') as file:
	number_twos = 0
	number_threes = 0
	for x in file:
		counted_two = False
		counted_three = False
		letters_occs = {}
		for let in x:
			if let in letters_occs:
				letters_occs[let] += 1
			else:
				letters_occs[let] = 1
		for key, value in letters_occs.items():
			# check for a 2 or 3 value to count
			if value==2 and counted_two==False:
				number_twos += 1
				counted_two = True
			elif value==3 and counted_three==False:
				number_threes += 1
				counted_three = True
			# we have counted max twos and threes for this ID now
			if counted_two and counted_three:
				break
	checksum = number_twos * number_threes
	print("checksum:",checksum)


# challenge 2
with open('input.txt', 'r') as file:
	inputs = []
	for x in file:
		inputs.append(x)
	result = ""
	for x in inputs:
		for y in inputs:
			if x==y:
				continue
			diffs = 0
			diff_pos = None
			for c_ptr in range(0,len(x)):
				if x[c_ptr]!=y[c_ptr]:
					diffs += 1
					diff_pos = c_ptr
			if diffs==1:
				for r_ptr in range(0,len(x)-1):
					if r_ptr!=diff_pos:
						result += str(x[r_ptr])
			if result != "":
				break
		if result != "":
			break
	print("result is:",result)













