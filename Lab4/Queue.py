class Queue:

    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.list[0]

    def push(self, element):
        self.list.append(element)

    def get_items(self):
        return self.list.copy()
