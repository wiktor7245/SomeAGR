
f = open('keysInsert.txt', 'r')
keysIns = f.read().split(' ')
l = [int(num) for num in keysIns]

file2 = open('keysDelete.txt', 'r')
keysDel = file2.read().split(' ')
d = [int(num) for num in keysDel]

class Node(object):

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    print("Dodalismy: " + str(data) + " , wys.: " + str(bst.height(bst)-1))
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    print("Dodalismy: " + str(data) + " , wys.: " + str(bst.height(bst)-1))
                else:
                    self.right.insert(data)
            else:
                print("Wierzcholek o kluczu " + str(data) + " juz istnieje")
        else:
            self.data = data
            print("Dodalismy: " + str(data) + " , wys.: " + str(bst.height(bst)-1))

    def lookup(self, data, parent=None):

        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    def delete(self, data):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            # deleting node with one child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

    def compare_trees(self, node):

        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):

        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    #the is sth wrong there
    #when i remove + 1 it returns 0
    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

for nr in l:
    if l.index(nr) == 0:
        bst = Node(l[0])
        print("Dodalismy: " + str(nr) + " , wys.: " + str(bst.height(bst)-1))
    else:
        bst.insert(nr)

print()

for nr in d:
    if None in bst.lookup(nr):
        print("Klucza " + str(nr) + " nie ma w drzewie")
    else:
        bst.delete(nr)
        print("Usunelismy: " + str(nr) + " , wys: " + str(bst.height(bst) - 1))