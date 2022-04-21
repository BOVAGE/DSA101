from collections import deque
from inspect import stack

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.peek()) # 5
    print(s.is_empty()) # False
    print(s.size()) # 5
    print(s.pop()) # 5
    print(s.pop()) # 4
    print(s.pop()) # 3
    print(s.pop()) # 2
    print(s.pop()) # 1
    s.is_empty() # True
    print(s.pop()) # index error 
