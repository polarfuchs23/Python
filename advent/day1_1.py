import os


folder_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{folder_path}\\inputs\\day1.txt', 'r') as f:
	input_list = f.read().split('\n')
	pass

loads = []
temp_sum = 0

for e in input_list:
	if e == '':
		loads.append(temp_sum)
		temp_sum = 0
	else:
		temp_sum += int(e)

print(max(loads))