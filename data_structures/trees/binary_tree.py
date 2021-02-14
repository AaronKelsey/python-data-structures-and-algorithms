from typing import List
from collections import deque


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

    def preorder(self, root: Node, output: List):
        if root:
            output.append(root.data)
            self.preorder(root.left, output)
            self.preorder(root.right, output)

        return output

    def postorder(self, root: Node, output: List):
        if root:
            self.postorder(root.left, output)
            self.postorder(root.right, output)
            output.append(root.data)

        return output

    def level_order(self, root):
        queue = deque()
        output = list()

        if root is None:
            return list()

        queue.append(root)

        while queue:
            node = queue.popleft()
            output.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return output


if __name__ == '__main__':
    tree = Tree(Node(1))

    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    ordered_output = []

    tree.inorder(tree.root, ordered_output)
    print(ordered_output)
    ordered_output.clear()

    tree.preorder(tree.root, ordered_output)
    print(ordered_output)
    ordered_output.clear()

    tree.postorder(tree.root, ordered_output)
    print(ordered_output)
    ordered_output.clear()

    print(tree.level_order(tree.root))
