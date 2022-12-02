import time

def isPrime(n):
	for i in range(2, int(n**0.5 + 1)):
		if n%i == 0:
			return False
	return True

def sieve(n):
	nums = set(range(2, n + 1))
	primes = set()
	while len(nums) > 0:
		num = nums.pop()
		primes.add(num)
		if n > num * num:
			nums.difference_update(set([*range(num, n+1, num)]))
		pass
	return list(primes)

def get_primes3(n):
	array = [i for i in range(n + 1)]	

	primes = [2]
	while True:
		last_prime = primes[len(primes) - 1]
		for i in range(last_prime, n, last_prime):
			array[i] = -1	

		for i in range(last_prime + 1, n):
			if array[i] != -1:
				primes.append(array[i])
				break
		else:
			return primes

def get_primes4(n):
	array = [i for i in range(n + 1)]	

	primes = [2]
	while True:
		last_prime = primes[len(primes) - 1]
		if n > last_prime * last_prime:
			for i in range(last_prime, n, last_prime):
				array[i] = -1	

		for i in range(last_prime + 1, n):
			if array[i] != -1:
				primes.append(array[i])
				break
		else:
			return primes

if __name__ == "__main__":
	start = time.time()
	test1 = get_primes3(1000000)
	print(time.time()-start)
	start = time.time()
	test2 = get_primes4(1000000)
	print(time.time()-start)
	print(sorted(test1) == sorted(test2))
