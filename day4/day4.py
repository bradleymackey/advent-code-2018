# advent of code day 4
# bradleymackey

# both challenges

def parse_data_from_file(input_file):
	"""
	`entries` are tuples of ints (index,formatted_time_number) e.g. (202, 151802240029)
	`actions` are the things that happen, as a list of strings: ['Guard', '#887', 'begins', 'shift']
	`entries` are sorted on return according to time value, actions are not (but the indicies do correspond, use index to lookup)
	"""
	entries = []
	actions = []
	
	# iterate over all input lines, extracting the action string and date for each
	index = 0
	for x in file:
		bits = x.split()
		# package together the time and index this appears in
		# transform the date/times from the form: 
		# 	[1518-02-24 00:29]
		# to the form:
		# 	151802240029
		# this allows us to more easily sort and do time arithmetic (all from the same format!)
		# (no guard starts sleeping on 23:xx, so arithmetic will work fine)
		date_joined = "".join(bits[0][1:].split('-'))
		time_joined = "".join(bits[1][:-1].split(':'))
		cron_num = int(date_joined+time_joined)
		entries.append((index,cron_num))
		actions.append(bits[2:])
		index += 1

	# sort all entries to chronological order
	# actions remain unsorted, lookup by key
	entries = sorted(entries, key=lambda tup : tup[1])
	return (entries, actions)

def calculate_guard_schedules(entries, actions):
	"""
	`guard_schedule` is a dict mapping guard number to a dict mapping minutes to how many minutes a guard was sleeping
	`guard_sleep_time` is a dict mapping guard number to the total number of minutes that guard was sleeping
	"""
	guard_schedule = defaultdict(lambda: defaultdict(int))
	guard_sleep_time = defaultdict(int)
	refers_to_guard = None
	guard_start_sleep = None
	for time in entries:
		index = time[0]
		time_val = time[1]
		first_word = actions[index][0]
		if first_word=="Guard":
			refers_to_guard = int(actions[index][1][1:])
		elif first_word=="falls":
			guard_start_sleep = time_val
		elif first_word=="wakes":
			# guards never start falling asleep if the time starts 23:xx, so this subtraction logic is fine
			time_asleep = time_val-guard_start_sleep
			guard_sleep_time[refers_to_guard] += time_asleep
			start_sleep_mins = int(str(guard_start_sleep)[-2:])
			for i in range(start_sleep_mins,start_sleep_mins+time_asleep):
				guard_schedule[refers_to_guard][i] += 1
		else:
			print("INVALID FIRST WORD:",first_word)
			exit()
	return (guard_schedule,guard_sleep_time)


with open('input.txt', 'r') as file:


	# calculate guard schedules using the inputs
	entries, actions = parse_data_from_file(file)
	guard_schedule, guard_sleep_time = calculate_guard_schedules(entries, actions)


	# ----- CHALLENGE 1 ------

	print(" ---> strategy 1:")

	# find the guard that sleeps the most overall
	most_sleep_guard = 0
	most_sleep_guard_time = 0
	for key,val in guard_sleep_time.items():
		if val>most_sleep_guard_time:
			most_sleep_guard_time = val
			most_sleep_guard = key
	print("the most sleepy guard is #",most_sleep_guard,"with",most_sleep_guard_time,"mins")
	best_time = 0
	best_time_occs = 0
	for key, val in guard_schedule[most_sleep_guard].items():
		if val>best_time_occs:
			best_time_occs = val
			best_time = key
	print("the best time to sneak is minute",best_time,"with",best_time_occs,"occurences")
	answer = most_sleep_guard*best_time
	print("challenge 1 answer =",most_sleep_guard,"*",best_time,"=",answer)


	# ----- CHALLENGE 2 -----

	print(" ---> strategy 2:")

	# find the minute that a guard sleeps the most on vs. all other guards and all other minutes
	chosen_minute = 0
	most_minute_occs = 0
	chosen_guard = 0
	for guard, times_asleep in guard_schedule.items():
		for sleep_min, occs in times_asleep.items():
			if occs>most_minute_occs:
				most_minute_occs = occs
				chosen_minute = sleep_min
				chosen_guard = guard
	print("guard #",chosen_guard,"sleeps on minute",chosen_minute,"more than any other guard on any other minute -",most_minute_occs,"times!")
	answer = chosen_guard*chosen_minute
	print("challenge 2 answer =",chosen_guard,"*",chosen_minute,"=",answer)



