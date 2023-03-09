


def unimodmax(check_list):
	compare_list = []
	for i in range(len(check_list) - 1):
		print(check_list[i])
		if check_list[i] < check_list[i + 1]:
			compare_list.append(-1)
			pass
		elif check_list[i + 1] == check_list[i]:
			compare_list.append(0)
			pass
		else:
			compare_list.append(1)
			pass
	print(compare_list)
	longest_interval_len = 0
	while 0 < len(compare_list):
		start0 = len(compare_list)
		start1 = len(compare_list)
		turn = 0
		if 0 in compare_list:
			start0 = compare_list.index(0)
		if -1 in compare_list:
			start1 = compare_list.index(-1)
		if start0 < start1:
			start = start0
		else:
			start = start1
		if 1 in compare_list:
			turn = compare_list.index(1)
		else:
			break
		if -1 in compare_list[turn:]:
			end = compare_list[turn:].index(-1)
		else:
			end = len(compare_list) - 1
		if longest_interval_len < (end - start + 1):
			longest_interval_len = (end - start + 1)
		compare_list = compare_list[turn:]
		print(compare_list)
		pass
	return longest_interval_len

if __name__ == "__main__":
	print(unimodmax([4,5,3,2,1,3,6,4,7]))
	print(unimodmax([10,9,8,10,6,5,4,3,2,3]))
	print(unimodmax([10,9,8,7,6,5,4,3,2,3]))