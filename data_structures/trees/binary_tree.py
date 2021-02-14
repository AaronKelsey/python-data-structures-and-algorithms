from typing import List


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def inorder(self, root: Node, output: List):
        if root:
            self.inorder(root.left, output)
            output.append(root.data)
            self.inorder(root.right, output)

        return output


if __name__ == '__main__':
    tree = Tree(Node(1))

    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)


    output = []

    tree.inorder(tree.root, output)

    print(output)
