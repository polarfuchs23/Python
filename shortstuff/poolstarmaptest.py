from multiprocessing import Pool


def test_func(a):
	return a

if __name__ == "__main__":
	with Pool(10) as p:
		result = p.map_async(test_func, range(10))
		print(type(result), result)
	pass