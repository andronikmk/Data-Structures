"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# import array as arr

# class Queue:
#     def __init__(self):
#         # self.size = 0
#         self.storage = [] # arr.array('i', [])
    
#     def __len__(self):
#         return(len(self.storage))

#     def enqueue(self, value):
#         # self.storage.append(value)
#         self.storage.extend([value])

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(0)


# Queue with an array

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size >= 1:
#             value = self.storage.pop(0)
#             self.size -= 1
#             return value

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size >= 1:
#            value = self.storage.pop(0)
#            self.size -= 1
#            return value


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size >= 1:
#            value = self.storage.pop(0)
#            self.size -= 1
#            return value


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#        self.storage.append(value)
#        self.size += 1

#     def dequeue(self):
#         if self.size >= 1:
#            value = self.storage.pop(0)
#            self.size -= 1
#            return value