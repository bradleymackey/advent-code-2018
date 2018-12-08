# advent of code day 1
# bradleymackey

# challenge 1
total = 0
with open('input.txt', 'r') as file:
	for x in file:
		try:
			number = int(x)
			total += number
		except:
			print("cannot extract number",x)
print("challenge 1 total:",total)


# challenge 2
total = 0
with open('input.txt', 'r') as file:
	seen = {0}
	found = False
	while found==False:
		file.seek(0) # file go back to start after a full loop
		for x in file:
			try:
				number = int(x)
				total += number
				if total in seen:
					print("challenge 2 first repeated value:",total)
					found = True
					break
				seen.add(total)
			except:
				print("cannot extract number",x)

