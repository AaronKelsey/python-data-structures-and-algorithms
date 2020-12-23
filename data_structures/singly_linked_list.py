class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f'({self.data})'


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')


# Example of the linked list being used
if __name__ == '__main__':
    linked_list = LinkedList()
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
