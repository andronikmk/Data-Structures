# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.perv = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     def add_to_head(self, value):
#         self.length += 1
#         if self.head is None:
#             self.head = ListNode(value)
#             self.tail = self.head

#         else:
#             new_head = ListNode(value, next=self.head)
#             self.head.prev = new_head
#             self.head = new_head
    
#     def remove_from_head(self):
#         if self.head is None:
#             return None

#         else:
#             self.length -= 1
#             value = self.head.value
#             self.head = self.head.next
#             if self.head is None:
#                 self.tail = None
#             else:
#                 self.head.prev = None
#             return value

#     def add_to_tail(self, value):
#         if self.tail is None:
#             self.add_to_head(value)
#         else:
#             self.length += 1
#             new_tail = ListNode(value, prev=self.tail)
#             self.tail.next = new_tail
#             self.tail = new_tail

    
#     def remove_from_tail(self):
#         if self.tail is None:
#             return None
#         else:
#             self.length -= 1
#             value = self.tail.value
#             self.tail = self.tail.prev
#             if self.tail is None:
#                 self.head = None
#             else:
#                 self.tail.next = None

#     def move_to_front(self, node):
#         self.add_to_head(node.value)
#         self.delete(node)

#     def move_to_end(self, node):
#         self.add_to_tail(node.value)
#         self.delete(node)

#     def delete(self, node):
#         if node.prev is None:
#             self.remove_from_head()
#         elif node.next is None:
#             self.remove_from_tail()
#         else:
#             self.length -= 1
#             node.prev.next = node.next
#             node.next.prev = node.prev

#     def get_max(self):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             max_value = self.head.value
#             while current.next is not None:
#                 current = current.next
#                 max_value - max(max_value, current.value)
#             return max_value
        

# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev

# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     def add_to_head(self, value):
#         self.lenght += 1
#         if self.head is None:
#             self.head = ListNode(value)
#             self.tail = self.head
#         else:
#             new_head = ListNode(value, next=self.head)
#             self.head.prev = new_head
#             self.head = new_head

#     def remove_from_head(self):
#         if self.head is None:
#             return None
#         else:
#             self.length -= 1
#             value = self.head.value
#             self.head = self.head.next
#             if self.head is None:
#                 self.tail = None
#             else:
#                 self.head.prev = None
#             return value

#     def add_to_tail(self, value):
#         if self.tail is None:
#             self.add_to_head(value)
#         else:
#             self.length += 1
#             new_tail = ListNode(value, prev=self.tail)
#             self.tail.next = new_tail
#             self.tail = new_tail

#     def remove_from_tail(self):
#         if self.tail is None:
#             return None
#         else:
#             self.length -= 1
#             value = self.tail.value
#             self.tail = self.tail.prev
#             if self.tail is None:
#                 self.head = None
#             else:
#                 self.tail.next = None
#             return value

#     def move_to_front(self, node):
#         self.add_to_tail(node.value)
#         self.delete(node)

#     def move_to_end(self, node):
#         self.add_to_tail(node.value)
#         self.delete(node)

#     def delete(self, node):
#         if node.prev is None:
#             self.remove_from_head()
#         elif node.next is None:
#             self.remove_from_tail()
#         else:
#             self.length -= 1
#             node.prev.next = node.next
#             node.next.prev = node.prev

#     def get_max(self):
#         if self.head is None:
#             return None
#         else:
#             current = self.head
#             max_value = self.head.value
#             while current.next is not None:
#                 current = current.next
#                 max_value = max(max_value, current.value)
#             return max_value


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_length(self, value):
        self.length += 1
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            new_head = ListNode(value, next=self.head)
            self.head.prev = new_head
            self.head = new_head

    def remove_from_head(self):
        if self.head is None:
            return None
        else:
            self.length -= 1
            value = self.head.value
            self.head = self.head.value
            if self.head is None:
                self.tail = None
            else:
                self.tail.prev = None
            return value

    def add_to_tail(self, value):
        if self.tail is None:
            self.add_to_head(value)
        else:
            self.length += 1
            new_tail = ListNode(value, prev=self.tail)
            self.tail.next = new_tail
            self.tail = new_tail
    
    def remove_from_tail(self):
        if self.tail is None:
            return None
        else:
            self.length -= 1
            value = self.tail.value
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            return value

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    def delete(self, node):
        if node.prev is None:
            self.remove_from_head()
        elif node.next is None:
            self.remove_from_tail()
        else:
            self.lenght -= 1
            node.prev.next = node.next
            node.next.prev = node.prev

    def get_max(self):
        if self.head is None:
            return None

        else:
            current = self.head
            max_value = self.head.value
            while current.next is not None:
                current = current.next
                max_value = max(max_value, current.value)
            return max_value