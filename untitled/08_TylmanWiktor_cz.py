
class Graph:
    def __init__(self, v):
        self.neighbours = []
        self.saturated = False
        for i in range(0, len(v)):
            if v[i] == 1:
                self.neighbours.append(i)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False

        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def minValueNode(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

    def delete(self, data):
        if self is None:
            return None
        if data < self.value:
            self.left = self.left.delete(data)
        elif data > self.value:
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp

            temp = self.minValueNode(self.right)
            self.value = temp.value
            self.right = self.right.delete(temp.value)

        return self

    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1


class a08_TeskeKarol_pn(object):
    matrix = []
    graph = []
    rotateMatrix = []
    saturate = []
    path = ""
    f = 0


    def run(self):
        self.matrix = self.read('Matching0.txt')
        self.rotate(self.matrix)
        self.prepareSaturateMatrix()
        self.getAssociations()

    def prepareSaturateMatrix(self):
        for i in range(0, len(self.rotateMatrix)):
            self.graph.append(Graph(self.rotateMatrix[i]))
            self.saturate.append(-1)

    def getAssociations(self):
        for i in range(0, len(self.graph)):
            for j in range(0, len(self.graph[i].neighbours)):
                if (self.saturateCheck(self.graph[i].neighbours[j]) and self.graph[i].saturated == False):
                    self.mPatch(i, j)
            if self.graph[i].saturated == False:
                self.f = 0
                while self.graph[i].saturated == False and self.f <= len(self.graph[i].neighbours):
                    for k in range(i, 0, -1):
                        for l in range(0, len(self.graph[k].neighbours)):
                            if self.saturateCheck(self.graph[k].neighbours[l]):
                                self.f += 1
                                self.saturate[k] = self.graph[k].neighbours[l]
                                self.path += str(self.graph[k].neighbours[l] + 1) + " " + str(k + 1) + " "
                                self.graph[k].saturated = True
                                k = -1
                                break
                        if k == -1:
                            break
                if self.saturate[i] != -1:
                    print("Ściezka M-zasilona:" + self.path[::-1])
                    self.path = ""
            if self.saturate[i] != -1:
                print("Aktualne skojarzenie: " + self.actualSaturate(self.saturate))
        if self.check(self.saturate):
            print("Znaleźlismy skojarzenie nasycające zbior X:\n Aktualne skojarzenie: " + self.actualSaturate(self.saturate))
        else:
            print("Nie ma skojarzenia w grafie.")

    def read(self, path):
        file = open(path, "r")
        data = file.readlines()
        matrix = []
        for i in range(len(data)):
            arr = list(map(str, data[i].split()))
            for j in range(len(arr)):
                arr[j] = int(arr[j])
            matrix.append(arr)
        return matrix

    def mPatch(self, i, j):
        self.saturate[i] = self.graph[i].neighbours[j]
        print("Ściezka M-zasilona: " + str(i + 1) + " " + str(self.graph[i].neighbours[j] + 1))
        self.graph[i].saturated = True


    def rotate(self, matrix):
        for i in range(0, len(matrix)):
            self.rotateMatrix.append([])
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                self.rotateMatrix[j].append(matrix[i][j])

    def saturateCheck(self, index):
        for i in range(0, len(self.saturate)):
            if self.saturate[i] == index:
                return False
        return True


    def isPathAvailable(self, a):
        for i in range(0, len(a)):
            if a[i] == -1:
                return False
        return True

    def actualSaturate(self, m):
        s = ""
        for i in range(0, len(m)):
            if m[i] != -1:
                s += "(" + str(i + 1) + "," + str(m[i] + 1) + ") "
        return s

    def check(self, m):
        for i in range(0, len(m)):
            if m[i] == -1:
                return False
        return True

if __name__ == '__main__':
   a08_TeskeKarol_pn().run()
