class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    class Node:
        def __init__(self, content, lower):
            self.content = content
            self.lower = lower

    def push(self, content):
        self.top = self.Node(content, self.top)
        self.size += 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def pop(self):
        if not self.is_empty():
            data = self.top
            self.top = self.top.lower
            self.size -= 1
            return data.content

    def peek(self):
        if not self.is_empty():
            return self.top



