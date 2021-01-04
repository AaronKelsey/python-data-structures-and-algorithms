class MaxHeap:
    def __init__(self, items=None):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__float_up(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max_node = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max_node = self.heap.pop()
        else:
            max_node = False
        return max_node

    def __swap(self, node_a, node_b):
        self.heap[node_a], self.heap[node_b] = self.heap[node_b], self.heap[node_a]

    def __float_up(self, index):
        parent = index//2

        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def __str__(self):
        return str(self.heap[0:len(self.heap)])


if __name__ == '__main__':
    max_heap = MaxHeap([6, 19, 10, 4, 27])
    max_heap.push(21)
    max_heap.push(11)

    print(max_heap)
    print(str(max_heap.pop()))
    print(max_heap)
    print(str(max_heap.pop()))
