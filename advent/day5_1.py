import os


folder_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{folder_path}\\inputs\\day5.txt', 'r') as f:
	input_list = f.read().split('\n')
	pass
stacks = []
for i in range(len(input_list)):
	print(input_list[i])
	if input_list[i] == '':
		stacks = input_list[:(i-1)]
		queries = input_list[(i+1):]
		break
		pass
	pass
test = len(stacks[0])//4
print(test)
towers = [[]] * int(len(stacks[0])//4 + 1)
print(towers)
for level in stacks[::-1]:
	for i in range(1, len(level) - 1, 4):
		print(level[i], i)
		if not level[i] == ' ':
			print(i//4)
			towers[i//4].append(level[i])
			print(towers[i//4], towers)
for tower in towers:
	print("tower: ",tower)