# advent of code day 5
# bradleymackey


# both challenges

def compact_polymer_removing_char(package):
	"""
	calculate the polymer deduction, removing a char beforehand (pass '' to remove no char)
	parameter should be a tuple (`string`,`char`), where `string` is the initial string and `char` is the char to remove
	"""
	# better method inspired by: https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4jzni/
	# i was too caught up to realise this is in no way whatsoever a >O(n^2) problem, which is what I made it
	string = package[0]
	char = package[1]
	stack = ['-']
	for c in string:
		j = stack[-1]
		# if we are removing this character, totally ignore it
		if c.lower() == char:
			continue
		elif c != j and j.lower() == c.lower():
			stack.pop()
		else:
			stack.append(c)
	return len(stack) - 1


from string import ascii_lowercase
import itertools
from multiprocessing import Pool

with open('input.txt', 'r') as file:

	# scan left to right, as per the docs
	# this should be very fast to run now!

	# ----- challenge 1 -----

	# strip the input string or risk an off-by-one error!
	# <very annoying>
	string = file.readline().strip()
	# we use the same function for challenge 1 and challenge 2
	# pass an empty char, because we do not want to initially remove any char
	answer = compact_polymer_removing_char((string,''))
	print("challenge 1:",answer)

	# ----- challenge 2 -----

	# multithreading to way speed this up!
	# thanks to https://stackoverflow.com/a/28463266/3261161

	# make the Pool of workers
	# ... giving each char its own thread
	pool = Pool(len(ascii_lowercase))

	# give each character it's own thread, also passing in the original string as well
	# and return the results
	results = pool.map(compact_polymer_removing_char, zip(itertools.repeat(string), ascii_lowercase))

	# close the pool and wait for the work to finish 
	pool.close() 
	pool.join()

	# result is the minimum
	answer = min(results)
	answer_char = ascii_lowercase[results.index(answer)]
	print("challenge 2:",answer,"(from char '"+answer_char+"')")
