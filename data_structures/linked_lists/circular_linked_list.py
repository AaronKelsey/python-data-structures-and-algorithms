class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'({self.data})'


class CircularLinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data, None)
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root

        while this_node is not None:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.rooot.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()


# Example of the circular linked list being used
if __name__ == '__main__':
    circular_linked_list = CircularLinkedList()
    circular_linked_list.add(2)
    circular_linked_list.add(4)
    circular_linked_list.add(6)
    circular_linked_list.add(8)
    circular_linked_list.print_list()

    print(f'size={circular_linked_list.size}')
    circular_linked_list.remove(6)
    print(f'size={circular_linked_list.size}')
    print(circular_linked_list.find(4))
    print(circular_linked_list.find(10))

    my_node = circular_linked_list.root
    for item in range(8):
        my_node = my_node.next_node
        print(my_node, end='->')
    print()
