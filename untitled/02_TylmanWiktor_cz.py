from collections import defaultdict

f = open('matrixDFS.txt', 'r')

# Converting file to list, # of edges
edgeCounter = 0;
l = [[int(num) for num in line.split(' ')] for line in f]
print("Macierz wejściowa:")
for k in l:
    edgeCounter += 1
    print(k)

print("#########################################################")
#converting matrix to dictionary with key of vertexes and values of vertexes connected to the vertex in key
d = defaultdict(list)
for position, item in enumerate(l):
    for position2, item2 in enumerate(item):
        if item2 == 1:
            d[position].append(position2)
print("Słownik stworzony z macierzy: ",d)

print("#########################################################")
def connected_components(graph):
    numofskl = 0
    seen = set()
    visited = []
    def dfs(v):
        vs = set([v])
        component=[]
        while vs:
            v = vs.pop()
            seen.add(v)
            vs |= set(graph[v]) - seen
            component.append(v)
            visited.append(v)
        return component
    ans=[]
    for v in graph:
        if v not in seen:
            numofskl = numofskl + 1
            d=dfs(v)
            ans.append(d)
    print("Liczba skladowych spojnosci",numofskl)
    print("Odwiedzone wierzcholki: ",visited)
    return ans
print("Skladowe spojnosci",connected_components(d))
