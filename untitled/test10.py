from copy import deepcopy

def fleury(graph, current, path, mx):
    if len(path) == mx + 1 and path[0] == path[-1]:
        return path
    for i, _ in graph[current].items():
        gp = deepcopy(graph)
        gp[current].pop(i)
        gp[i].pop(current)
        p = fleury(gp, i, path + [i], mx)
        if p:
            return p
    return None

matrix = [[int(x) if x != '-' else '-' for x in line.split(' ') if len(x)] for line in open('Chinski2.txt').read().split('\n') if len(line)]
verts = {ind: { i: x for i, x in enumerate(line) if x != '-' and i != ind} for ind, line in enumerate(matrix)}
print('stopien', { i: len(l) for i, l in verts.items() })
su = sum([len(l) for i, l in verts.items()])
print('suma', su)
print(fleury(deepcopy(verts), 0, [0], su / 2))