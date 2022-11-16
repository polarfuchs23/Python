def roots(a, b, c, d, e, f):
	koef_list = [1, 2, 3, 4, 5, 6]

	prev_is_pos = True
	counter = 0
	for k in koef_list:
		if (k < 0) == prev_is_pos:
			counter += 1
			prev_is_pos = not prev_is_pos
			pass
		pass

	return