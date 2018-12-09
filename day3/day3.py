# advent of code day 3
# bradleymackey

from collections import defaultdict

# challenge 1
with open('input.txt', 'r') as file:
	# add 1 to the position for each claim
	positions = defaultdict(int)
	# extract all offsets and sizes from the doc
	for x in file:
		bits = x.split()
		inset = bits[2][0:-1].split(',')
		x, y = tuple(map(int,inset))
		size = bits[3].split('x')
		w, h = tuple(map(int,size))
		for i in range(x, x+w):
			for j in range(y, y+h):
				positions[(i,j)] += 1
	# answer is the number of sections with more than one claim per squ.in.
	answer = 0
	for key,val in positions.items():
		if val>1:
			answer += 1
	print("challenge 1 answer:",answer)


# challenge 2
with open('input.txt', 'r') as file:
	# add 1 to the position for each claim
	claimed_by = defaultdict(list)
	# extract all offsets and sizes from the doc
	claim_num = 1
	for x in file:
		bits = x.split()
		inset = bits[2][0:-1].split(',')
		x, y = tuple(map(int,inset))
		size = bits[3].split('x')
		w, h = tuple(map(int,size))
		for i in range(x, x+w):
			for j in range(y, y+h):
				claimed_by[(i,j)] += [claim_num]
		claim_num += 1
	# answer is the only one that has all it's claims as the only claim for each given square
	single_claims = set()
	impossible_candidates = set()
	for key,val in claimed_by.items():
		if len(val)==1:
			# this has the potential of being right!
			# ensure that any of the other bits of it are not disputed
			if val[0] not in impossible_candidates:
				single_claims.add(val[0])
		else:
			for item in val:
				# all these items are in disputed teritory
				# none of them can be the answer
				impossible_candidates.add(item)
				if item in single_claims:
					single_claims.remove(item)
	print("challenge 2 candidates:",single_claims)

