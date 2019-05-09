import math

f = open("FindForest.txt", "r")
l= f.read().splitlines()

graph = {}
i = 1
for line in l:
	newLine = line.split()
	graph[i] = {}
	j = 1
	for weight in newLine:
		if weight != '-' and j != i:
			graph[i][j] = int(weight)
		j += 1
	i += 1

def findforest():
	# (previous, distance)
	dist_tuple = {}
	#there was sth wrong and i had to give math.inf on the end
	for i in range(1, len(graph) + 1):
		dist_tuple[i] = (0, math.inf)

	not_visited = list(range(1, len(graph) + 1))
	com_i = -1
	com_v = []
	while not_visited:
		# nv == not_visitedd
		not_visitedd = [d for d in dist_tuple.items() if d[0] in not_visited]
		sort_not_visitedd = sorted(not_visitedd, key = lambda d:d[1][1])
		first_not_visitedd = sort_not_visitedd[0][0]
		not_added_neigh = [item for item in graph[first_not_visitedd].items()\
		if item[0] in not_visited]
		for adj_v, distance in not_added_neigh:
			if dist_tuple[adj_v][1] > distance:
				dist_tuple[adj_v] = (first_not_visitedd, distance)
		not_visited.remove(first_not_visitedd)

		visited_adj_v = [v for v in graph[first_not_visitedd].keys()\
		if v not in not_visited]
		if not visited_adj_v:
			com_i += 1
			com_v.append([])

		com_v[com_i].append(first_not_visitedd)

	print("Wykorzystana metoda: III")
	com_e = []
	forest_weight = 0
	index = 0
	for com_ver in com_v:
		com_e.append([])
		weight = 0

		for vertex in com_ver:
			if dist_tuple[vertex][0] != 0 and\
			(dist_tuple[vertex][0], vertex) not in com_e[index]:
				com_e[index].append((vertex, dist_tuple[vertex][0]))
				weight += dist_tuple[vertex][1]

		forest_weight += weight
		index += 1
		print("DRZEWO " + str(index))
		print("Wierzchołki: " + str(sorted(com_ver)))
		print("Krawędzie: " + str(com_e[index - 1]))
		print("Waga drzewa: " + str(weight))
		print()
		print("Waga lasu: " + str(forest_weight))

findforest()
