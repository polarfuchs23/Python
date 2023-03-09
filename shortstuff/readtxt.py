import os

this_path = os.path.dirname(__file__)

with open(this_path + "/readtxt/test.txt", 'r') as f:
	test1 = f.readlines()
	test2 = list(map(lambda s: str(s).replace('\n', ''), f.readlines()))

print(test1)
print(test2)