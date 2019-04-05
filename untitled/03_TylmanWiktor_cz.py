import math

#input chooser
num = input("Choose 1,2 or 3 file by typing one of the numbers: ")
if num == '1' or num == '2' or num == '3':
	file = open("MatrixPaths" +  num +".txt", "r")
input_graph = file.read().splitlines()

#converting to dictionary
dijkstra = True
graph = {}
i = 1
for line in input_graph:
	newLine = line.split()
	graph[i] = {}
	j = 1
	for weight in newLine:
		if weight != '-' and j != i:
			graph[i][j] = int(weight)
			if int(weight) < 0:
				dijkstra = False
		j += 1
	i += 1

#dictionary with {distance,previous}
temp_table = {}
temp_table[1] = (0, 0)
for index in range(2, len(graph) + 1):
	temp_table[index] = (math.inf, 0)

#list whrere we store not visited vertexes
not_visited = list(range(len(graph)))

# relaxing egdes (vertex1, vertex2, weight)
def relax(u, v, weight):
	global table_data
	new_distance = temp_table[u][0] + weight
	if temp_table[v][0] > new_distance:
		temp_table[v] = (new_distance, u)
	return

#dijkstra alg
def dijkstra_alg(index):
	global not_visited
	global temp_table

	not_visited.remove(index)

	for adj_vertex, distance in graph[index].items():
		relax(index, adj_vertex, distance)

	#sorting and invoking
	if not_visited:
		sorted_by_distance = sorted(temp_table.items(), key=lambda d: d[1][0])
		for vertex_data in sorted_by_distance:
			if vertex_data[0] in not_visited:
				dijkstra_alg(vertex_data[0])
	return

def bellford_alg(index):
	global not_visited
	global temp_table

	#helper edges list (vetex1,vertex2, weight)
	edges = []
	for vertex_u in range(1, len(graph) + 1):
		for vertex_v, distance in graph[vertex_u].items():
			edges.append((vertex_u, vertex_v, distance))

	for i in range(1, len(graph)):
		for vertex in graph:
			for edge in edges:
				relax(*edge)

	for u, v, weight in edges:
		if temp_table[v][0] > temp_table[u][0] + weight:
			return False
	return True

def shortest_paths():
	global table_data
	print("Shortest path from 1 to:")
	for vertex in graph.keys():
		path = []
		current = vertex
		print(current, end = ": ")
		path.append(current)
		while current != 1:
			current = temp_table[current][1]
			path.append(current)
		path_to_print = list(reversed(path))
		for vertex in reversed(path):
			print(vertex, end = " ")
		print(" with the length of " + str(temp_table[vertex][0]))

if dijkstra:
	print("I am using Dijkstra algorithm!")
	print()
	dijkstra_alg(1)
	shortest_paths()
else:
	print("I am using Bellmana-Ford algorithm!")
	print()
	if bellford_alg(1):
		shortest_paths()
	else:
		print("Wykryto ujemny cykl - brak rozwiązania")
