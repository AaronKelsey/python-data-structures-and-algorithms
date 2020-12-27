class Node:

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return f'({self.data})'


class DoublyLinkedList:
    def __init__(self, root=None):
        self.root = root
        self.last = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.last = self.root
        else:
            new_node = Node(data, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            elif this_node.next_node is None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root

        while this_node is not None:
            if this_node.data == data:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()


# Example of the linked list being used
if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.add(2)
    linked_list.add(4)
    linked_list.add(6)
    linked_list.add(8)
    linked_list.print_list()

    print(f'size={linked_list.size}')
    linked_list.remove(6)
    print(f'size={linked_list.size}')
    print(linked_list.find(4))
    print(linked_list.root)
