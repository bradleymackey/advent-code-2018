# advent of code day 5
# bradleymackey

# both challenges
import re

def remove_pair(s, i):
    return s[:i] + s[i+2:]

def compact_polymer_removing_char(package):
	"""
	calculate the polymer deduction, removing a char beforehand (pass '' to remove no char)
	parameter should be a tuple (string,char), where string is the initial string and char is the char to remove
	"""
	string = package[0]
	char = package[1]
	lower = str(char).lower()
	upper = str(char).upper()
	new = re.sub(lower+"|"+upper,"",string)
	# print("now trying:",char,"string:",new)
	end = False
	while end==False:
		end = True
		for i in range(len(new)-1):
			index_reached = i
			char_one = str(new[i])
			char_two = str(new[i+1])
			if char_one.lower()==char_two.lower():
				if (char_one.isupper() and char_two.islower()) or (char_one.islower() and char_two.isupper()):
					new = remove_pair(new,i)
					if len(new)%10000 == 0:
						print("[UPDATE] current",char,"length is now",len(new))
					end = False
					break
	print(char,"result length is is",len(new))
	return len(new)


# challenge 1
with open('input.txt', 'r') as file:

	# scan left to right, as per the docs
	# this can take a few mins, depending on computer specs

	# strip the input string or risk an off-by-one error!
	# <very annoying>
	string = file.readline().strip()
	# we use the same function for challenge 1 and challenge 2
	# pass an empty char, because we do not want to initially remove any char
	answer = compact_polymer_removing_char((string,''))
	print("challenge 1 answer:",answer)



# challenge 2
import itertools
from multiprocessing import Pool
with open('input.txt', 'r') as file:

	# this will take longer to run!
	# multithreading should help though!
	# thanks to https://stackoverflow.com/a/28463266/3261161
	# (p.s. i found that the answer seems to pop out before the others have finished...)
	# (...so you can probably terminate early as soon as that first one is found)

	string = file.readline().strip()
	char_list = "abcdefghijklmnopqrstuvwxyz"

	# make the Pool of workers
	# ... giving each char its own thread
	pool = Pool(len(char_list))

	# give each character it's own thread, also passing in the original string as well
	# and return the results
	results = pool.map(compact_polymer_removing_char, zip(itertools.repeat(string), char_list))

	# close the pool and wait for the work to finish 
	pool.close() 
	pool.join()

	# zip each char back with its result
	result_data = zip(char_list,results)
		
	best_char = None
	best_len = None
	for char,length in result_data:
		if best_len==None or length<best_len:
			best_len = length
			best_char = char
	print("challenge 2 answer:",best_len,"(from char '"+best_char+"'')")
