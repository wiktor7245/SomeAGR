class Vertex:

    def __init__(self, name=None):
        self._edgeList = None
        self._name = name
        self._nextVertex = None
        self._visited = False

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setNextVertex(self, vertex):
        self._nextVertex = vertex

    def getNextVertex(self):
        return self._nextVertex

    def getTheEdgeList(self):
        return self._edgeList

    def setTheEdgeList(self, edge):
        self._edgeList = edge

    def setVisited(self, value):
        self._visited = value

    def getVisited(self):
        return self._visited


class Edge:
    def __init__(self, link):
        self._nextEdge = None
        self._link = link

    def setNextEdge(self, edge):
        self._nextEdge = edge

    def getNextEdge(self):
        return self._nextEdge

    def setLink(self, vertex):
        self._link = vertex

    def getLink(self):
        return self._link


class Graph:

    def __init__(self):
        self._head = None
        self._path = []

    def addVertex(self, data):
        ver = Vertex(data)
        ver.setNextVertex(self._head)
        self._head = ver

    def connect(self, a, b):
        ver = self._head
        firstVer = None
        secondVer = None
        while firstVer == None or secondVer == None:
            if ver.getName() == a and firstVer == None:
                firstVer = ver
            elif ver.getName() == b and secondVer == None:
                secondVer = ver
            ver = ver.getNextVertex()

        if firstVer.getTheEdgeList() == None:
            firstVer.setTheEdgeList(Edge(secondVer))
        else:
            cur = firstVer.getTheEdgeList()
            if cur.getNextEdge() != None:
                while cur.getNextEdge() != None:
                    cur = cur.getNextEdge()
            else:
                cur.setNextEdge(Edge(secondVer))

    def display(self):
        ver = self._head
        while ver != None:
            print("Vertex:" + ver.getName())
            cur = ver.getTheEdgeList()
            while cur != None:
                print("Edge of vertex:" + cur.getLink().getName())
                cur = cur.getNextEdge()
                if cur == None:
                    print()
            ver = ver.getNextVertex()

    def allVisited(self):
        ver = self._head
        while ver != None:
            if ver.getVisited() == False:
                return False
            ver = ver.getNextVertex()
        return True

    def HamiltonianCycle(self, startingPoint):
        ver = self._head
        while ver.getName() != startingPoint:
            ver = ver.getNextVertex()
        self.add(ver)
        ver.setVisited(True)
        if self.allVisited() == True:
            print("Start of the Path:")
            self.printAllPath()
            print("End of the Path")
            ver.setVisited(False)
            self.delete()
            return
        if ver.getTheEdgeList() == None:
            ver.setVisited(False)
            self.delete()
            return
        cur = ver.getTheEdgeList()
        while cur != None:
            if cur.getLink().getVisited() == False:
                self.HamiltonianCycle(cur.getLink().getName())
            cur = cur.getNextEdge()
        ver.setVisited(False)
        self.delete()
        return

    def checkForVisited(self):
        ver = self._head
        while ver != None:
            print(ver.getName(), ver.getVisited())
            ver = ver.getNextVertex()

    def add(self, data):
        self._path.append(data)

    def delete(self):
        del self._path[-1]

    def display(self):
        return print("Cur: " + self._path[-1].getName())

    def printAllPath(self):
        for a in range(0, len(self._path)):
            print(self._path[a].getName())


g = Graph()
g.addVertex("1")
g.addVertex("2")
g.addVertex("3")
g.addVertex("4")
g.addVertex("5")
g.addVertex("6")

g.connect("1", "2")
g.connect("2", "3")
g.connect("2", "5")
g.connect("3", "1")
g.connect("3", "4")
g.connect("4", "3")
g.connect("4", "6")
g.connect("5", "3")
g.connect("5", "4")
g.connect("6", "1")
g.connect("6", "2")
g.connect("6", "3")
g.HamiltonianCycle("1")