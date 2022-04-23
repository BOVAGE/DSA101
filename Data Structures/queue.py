from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0