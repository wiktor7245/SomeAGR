# 2a
print()
print("Zadanie 3: ")
print()

import math

# ODTWARZANIE STRUKTURY GRAFU
file = open("FindForest.txt", "r")
lines = file.read().splitlines()

graph = {}
i = 1
for line in lines:
	splittedLine = line.split()
	graph[i] = {}
	j = 1
	for weight in splittedLine:
		if weight != '-' and j != i:
			graph[i][j] = int(weight)
		j += 1
	i += 1

#------------------------------------------------------------------------------#

def prim_tree():
	# INICJALIZACJA TABELI POMOCNICZEJ
	table_data = {} # SŁOWNIK TUPLI (POPRZEDNIK, DYSTANS)
	# ZE WZGLĘDU NA OGRANICZENIA ALGORYTMU
	# ODLEGŁOŚCI KORZENI DO SIEBIE SAMYCH (0)
	# W KOŃCOWYM REZULTACIE ZAPISANE SĄ JAKO MATH.INF
	for index in range(1, len(graph) + 1):
		table_data[index] = (0, math.inf)

	# ZAPISANIE NIEODWIEDZONYCH WIERZCHOŁKÓW DO LISTY
	# ORAZ IMPLEMENTACJA LISTY SKŁADOWYCH
	not_visited = list(range(1, len(graph) + 1))
	components_index = -1
	components_vertices = []
	while not_visited:
		# nv == not_visited
		nv_table_data = [d for d in table_data.items() if d[0] in not_visited]
		sorted_nv_table_data = sorted(nv_table_data, key = lambda d:d[1][1])
		first_nv = sorted_nv_table_data[0][0]
		not_appended_neighbours = [item for item in graph[first_nv].items()\
		if item[0] in not_visited]
		for adjacent_vertex, distance in not_appended_neighbours:
			if table_data[adjacent_vertex][1] > distance:
				table_data[adjacent_vertex] = (first_nv, distance)
		not_visited.remove(first_nv)

		# JEŚLI WSZYSCY SĄSIEDZI SĄ NIEODWIEDZENI MAMY KOLEJNĄ SKŁADOWĄ
		visited_adjacent_vertices = [v for v in graph[first_nv].keys()\
		if v not in not_visited]
		if not visited_adjacent_vertices:
			components_index += 1
			components_vertices.append([])

		components_vertices[components_index].append(first_nv)

	print("WYKORZYSTANA METODA: III")
	components_edges = []
	forest_weight = 0
	index = 0
	for component_vertices in components_vertices:
		components_edges.append([])
		weight = 0

		for vertex in component_vertices:
			if table_data[vertex][0] != 0 and\
			(table_data[vertex][0], vertex) not in components_edges[index]:
				components_edges[index].append((vertex, table_data[vertex][0]))
				weight += table_data[vertex][1]

		forest_weight += weight
		index += 1
		print("DRZEWO " + str(index))
		print("Wierzchołki: " + str(sorted(component_vertices)))
		print("Krawędzie: " + str(components_edges[index - 1]))
		print("Waga drzewa: " + str(weight))
		print()
	print("Waga lasu: " + str(forest_weight))

#------------------------------------------------------------------------------#

prim_tree()
