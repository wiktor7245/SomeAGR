import copy

class Graph():
    def __init__(self, fileName):
        f = open(fileName, "r")
        self.matrix = []
        self.verticiesCounter = 0
        self.verticies = []
        self.weight = dict()
        for line in f:
            newLine = line.replace("\n", "")
            list = newLine.split()
            self.matrix.append(list)
            self.verticiesCounter += 1
            self.verticies.append(self.verticiesCounter)
            self.checkWeight()
            self.countDegree()

    def countDegree(self):
        self.degree = dict()
        li = 1
        for line in self.matrix:
            res = 0
            for character in line:
                if character != "" and character != "-" and character != "0":
                    res += 1
            self.degree[li] = res
            li += 1

    def checkWeight(self):
        vertexIndex = 1
        for line in self.matrix:
            c2 = 1
            weight = dict()
            for character in line:
                if character != "" and character != "-" and character != "0":
                    weight[c2] = int(character)
                c2 += 1
            self.weight[vertexIndex] = weight
            vertexIndex += 1

    def cpp(self):
        odd = 0
        for k, v in self.degree.items():
            if v % 2 != 0:
                odd += 1
        print("Liczba wierzcholkow o nieparzytym stopniu:")
        print(str(odd))
        if odd > 0:
            print("Graf nieeulerowski")
        else:
            print("Graf eulerowski")
            rejected = []
            result = []
            pos = self.verticies[0]
            result.append(pos)
            edgeWeight = copy.deepcopy(self.weight)
            while True:
                n = []
                for k, v in edgeWeight[pos].items():
                    n.append(k)
                if len(n) == 0:
                    break
                index = 0
                while True:
                    if index >= len(n):
                        result.append(n[0])
                        rejected.remove((pos, n[0]))
                        del edgeWeight[pos][n[0]]
                        del edgeWeight[n[0]][pos]
                        pos = n[0]
                        break
                    if self.isEdgeCut(pos, n[index], edgeWeight):
                        rejected.append((pos, n[index]))
                        index += 1
                    else:
                        result.append(n[index])
                        del edgeWeight[pos][n[index]]
                        del edgeWeight[n[index]][pos]
                        pos = n[index]
                        break
            print("Ignorowane krawedzie ciecia:")
            for tup in rejected:
                print(tup[0], tup[1])
            print("Rozwiazanie problemu chinskiego listonosza:")
            print(result)

    def isEdgeCut(self, v1, v2, edgeWeight):
        weightCopy = copy.deepcopy(edgeWeight)
        del weightCopy[v1][v2]
        del weightCopy[v2][v1]
        stack = []
        concomponents = []
        concomponent = []
        consideredEd = []
        consideredV = []
        w = self.verticies[0]
        stack.append(w)
        consideredV.append(w)
        concomponent.append(w)
        while True:
            n = []
            for k, v in weightCopy[w].items():
                n.append(k)
            j = 0
            while j != len(n):
                if ((n[j], w) and (w, n[j])) not in consideredEd:
                    consideredEd.append((n[j], w))
                    if (n[j]) not in consideredV:
                        w = n[j]
                        stack.append(w)
                        consideredV.append(w)
                        concomponent.append(w)
                        break
                j += 1
            if j == len(n):
                stack.remove(w)
                if len(stack) != 0:
                    w = stack[-1]
                else:
                    if len(self.verticies) == len(consideredV):
                        concomponents.append(concomponent)
                        break
                    else:
                        v = 0
                        while True:
                            if self.verticies[v] not in consideredV:
                                w = self.verticies[v]
                                stack.append(w)
                                consideredV.append(w)
                                concomponents.append(concomponent)
                                concomponent = []
                                concomponent.append(w)
                                break
                            v += 1
        ns = 0
        for i in concomponents:
            if len(i) > 1:
                ns += 1
        if ns > 1:
            return True
        else:
            return False


g = Graph("Chinski.txt")
g.cpp()