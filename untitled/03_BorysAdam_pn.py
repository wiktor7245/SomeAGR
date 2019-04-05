# 2a
print()
print("Zadanie 3: ")
print()

import math

# PRZETWARZANIE LINIJEK WYBRANEGO PLIKU TEKSTOWEGO Z MACIERZĄ GRAFU
file_number = 0
while int(file_number) not in range(1,4):
	file_number = input("Wybierz numer pliku macierzy (1-3): ")
print()

file = open("MatrixPaths0" + file_number +".txt", "r")
lines = file.read().splitlines()

# DETERMINACJA ALGORYTMU PRZY OKAZJI ODTWARZANIA STRUKTURY GRAFU
# W FORMIE ZAGNIEŻDŻONEGO SŁOWNIKA POSTACI:
# {wierzchołek1: {sąsiad1: waga, sąsiad2: waga, (...)}, wierzchołek2: {...}}
dijkstra = True # False <=> Bellman-Ford
graph = {}
i = 1
for line in lines:
	splittedLine = line.split()
	graph[i] = {}
	j = 1
	for weight in splittedLine:
		if weight != '-' and j != i:
			graph[i][j] = int(weight)
			if int(weight) < 0:
				dijkstra = False
		j += 1
	i += 1

# IMPLEMENTACJA TABELI POMOCNICZEJ DLA ALGORYTMÓW I
table_data = {} #SŁOWNIK TUPLI (DYSTANS, POPRZEDNIK)
table_data[1] = (0, 0)
for index in range(2, len(graph) + 1):
	table_data[index] = (math.inf, 0)

# ZAPISANIE NIEODWIEDZONYCH WIERCHOŁKÓW DO LISTY (Dijkstra)
not_visited = list(range(len(graph)))

# RELAKSACJA KRAWĘDZI DANEJ POSTACIĄ (U, V, WAGA)
def relax(u, v, weight):
	global table_data
	new_distance = table_data[u][0] + weight
	if table_data[v][0] > new_distance:
		table_data[v] = (new_distance, u)
	return

def dijkstra_paths(index):
	global not_visited
	global table_data

	not_visited.remove(index)

	for adjacent_vertex, distance in graph[index].items():
		relax(index, adjacent_vertex, distance)

	# SORTOWANIE I WYBÓR NAJBLIŻSZEGO NIEODWIEDZONEGO WIERZCHOŁKA ORAZ
	# REKURENCYJNE WYWOŁANIE FUNKCJI
	if not_visited:
		sorted_by_distance = sorted(table_data.items(), key=lambda d: d[1][0])
		for vertex_data in sorted_by_distance:
			if vertex_data[0] in not_visited:
				dijkstra_paths(vertex_data[0])
	return

def bellford_paths(index):
	global not_visited
	global table_data

	# TWORZENIE POMOCNICZEJ LISTY KRAWĘDZI POSTACI: (vertex_u, vertex_v, weight)
	edges = []
	for vertex_u in range(1, len(graph) + 1):
		for vertex_v, distance in graph[vertex_u].items():
			edges.append((vertex_u, vertex_v, distance))

	for i in range(1, len(graph)):
		for vertex in graph:
			for edge in edges:
				relax(*edge)

	for u, v, weight in edges:
		if table_data[v][0] > table_data[u][0] + weight:
			return False
	return True

def print_shortest_paths():
	global table_data
	print("Najkrótsza ścieżka z 1 do:")
	for vertex in graph.keys():
		path = []
		current = vertex
		print(current, end = ": ")
		path.append(current)
		while current != 1:
			current = table_data[current][1]
			path.append(current)
		path_to_print = list(reversed(path))
		for vertex in reversed(path):
			print(vertex, end = " ")
		print(" o długości " + str(table_data[vertex][0]))

if dijkstra:
	print("Wyłącznie wagi dodatnie (używam Dijkstry)")
	print()
	dijkstra_paths(1)
	print_shortest_paths()
else:
	print("Obecne wagi ujemne (używam Bellmana-Forda)")
	print()
	if bellford_paths(1):
		print_shortest_paths()
	else:
		print("Wykryto ujemny cykl - brak rozwiązania")
print()
