
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, value):
        #add to the end of the list
        self.storage.append(value)
        self.size += 1
        

    def dequeue(self):
        self.storage.pop(0)
        self.size -= 1
        

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def pop(self):
        self.size -= 1
        self.storage.pop(0)
