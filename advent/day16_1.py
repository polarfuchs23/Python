import os


#valve_flowrates = dict()
valve_connections = dict()


folder_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{folder_path}\\inputs\\day16.txt', 'r') as f:
	lines = f.read().split('\n')
	for l in lines:
		if l == '':
			break
		valve = l[6:8]
		flow_rate = l[l.index("rate=") + 5:l.index(';')]
		_, temp_connections = l.split("valve")
		connections = temp_connections.replace('s', '').replace(' ', '').split(',')
		connections.append(flow_rate)
		#valve_flowrates[valve] = flow_rate
		valve_connections[valve] = connections
	#valve_flowrates = dict(sorted(valve_flowrates.items()))
	valve_connections = dict(sorted(valve_connections.items()))
	#print(valve_flowrates)
	print(valve_connections)