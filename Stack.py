class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def pop(self):
        return self.stack.pop()
    def push(self,item):
        self.stack.append(item)
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[len(self.stack)-1]
    
