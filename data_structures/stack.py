class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peak(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def clear(self):
        self.stack.clear()

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack = Stack()

    for i in range(11):
        stack.push(i)

    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peak())
    stack.clear()
    print(stack)
