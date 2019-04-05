f = open('graph.txt', 'r')

# Converting file to list, # of edges
edgeCounter = 0;
l = [[int(num) for num in line.split(' ')] for line in f]
print("Input matrix:")
for k in l:
    edgeCounter += 1
    print(k)

print("\n# of edges: " + str(edgeCounter))

print("*******************************************")
# Marks
marks = []
bigMarkCounter, bigMarkPos = 0, 0
for i in range(edgeCounter):
    tempMark = l[i].count(1)
    marks.append(tempMark)
    if tempMark > bigMarkCounter:
        bigMarkCounter = tempMark
        bigMarkPos = i
print("Marks list", marks)

print("*******************************************")
# Vertices adjacent to the vertex with the highest degree
print("#Vertices adjacent to the vertex with the highest degree")
for i in range(edgeCounter):
    if l[bigMarkPos][i] == 1:
        print(i)

print("*******************************************")
# Edges
edges = []
print("Edges of the graph:")
for i in range(edgeCounter):
    for j in range(edgeCounter):
        if l[i][j] == 1:
            checkEdge = [j, i]
            if not checkEdge in edges:
                edge = [i, j]
                edges.append(edge)
print(edges)

print("*******************************************")
# Incidence matrix
print("Incidence matrix")
incidenceMatrix = [[0 for j in range(len(edges))] for i in range(edgeCounter)]
x = 0
for edge in edges:
    i = edge[0]
    j = edge[1]
    incidenceMatrix[i][x] = 1
    incidenceMatrix[j][x] = 1
    x += 1
for i in range(6):
    print(incidenceMatrix[i])

print("*******************************************")
# list of successors
print("list of successors")
successorsList = {
    "0": [],
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": []
}
for i in range(edgeCounter):
    x = []
    for j in range(edgeCounter):
        if l[i][j] == 1:
            x.append(j)
    j = str(i)
    successorsList[j] = x
for i in range(edgeCounter):
    j = str(i)
    print(j)
    print(successorsList[j])
