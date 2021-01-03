from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else:
            return None

    def peak(self):
        if self.size > 0:
            ret_val = self.queue.popleft()
            self.queue.appendleft(ret_val)
            return ret_val
        else:
            return None

    def get_size(self):
        return self.size

    def clear(self):
        self.queue.clear()

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    queue = Queue()

    for i in range(1, 11):
        queue.enqueue(i)

    print(queue)
    print(queue.get_size())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)

    print(queue.peak())
    print(queue)

    print(queue.get_size())
    queue.clear()
    print(queue)
