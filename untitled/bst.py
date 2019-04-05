f = open('keysInsert.txt', 'r')
keysIns = f.read().split(' ')
print(keysIns)
l = [int(num) for num in keysIns]
print(l)

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return False
            return self.right.findval(lkpval)
        else:
            return True

root = Node(l[0])
for nr in l:
    if l.index(nr) == 0:
        print("Dodalismy: " + str(nr))
    else:
        if root.findval(nr) == False:
            root.insert(nr)
            print("Dodalismy: " + str(nr))
        else:
            print("Wierzcholek o kluczu " + str(nr) + " juz istnieje")

root.PrintTree()