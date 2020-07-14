"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.list = []
        self.size = 0
        # self.storage = ?

    def __len__(self):
        return len(self.list)

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def __str__(self):
        return "{self.list}".format(self=self)


stack = Stack()
print(stack)

stack.push(4)
print(stack)

stack.push('item 2')
print(stack)

stack.push(8.60)
print(stack)

print(stack.pop())
print(stack)

