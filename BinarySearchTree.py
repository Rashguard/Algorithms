from __future__ import print_function


class Node:

    def __init__(self):
        self.p = None
        self.left = None
        self.right = None


class IntNode(Node):

    def __init__(self):
        super().__init__()
        self.key = 0

    def less_than(self, other):
        return self.key < other.key

    def make_node(self, key):
        n = IntNode()
        n.key = key
        return n

    def print_node(self):
        print(self.key)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.less_than(x):
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.less_than(y):
            y.left = z
        else:
            y.right = z

    def print_util(self, tree, level):
        if (tree.right):
            self.print_util(tree.right, level + 1)
        for i in range(level):
            print("    ", end='')
        tree.print_node()
        if (tree.left):
            self.print_util(tree.left, level + 1)

    def print_tree(self):
        self.print_util(self.root, 0)


def main():
    print("---- main ----")
    proto = IntNode()
    bst = BinarySearchTree()
    bst.insert(proto.make_node(9))
    bst.insert(proto.make_node(7))
    bst.insert(proto.make_node(8))
    bst.insert(proto.make_node(7))
    bst.insert(proto.make_node(7))
    bst.insert(proto.make_node(8))
    bst.insert(proto.make_node(9))
    bst.insert(proto.make_node(3))
    bst.insert(proto.make_node(1))
    bst.insert(proto.make_node(0))
    bst.print_tree()

main()
