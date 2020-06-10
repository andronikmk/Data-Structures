class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        self.value = value
    
    def get_next(self):
        self.next_node = next_node

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value


# ===========================================================================================

class Node:
    def __init__(self, value=None, next_node=None):
        # value of linked list node
        self.value = value
        # reference to next node in the list
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        # set this node's next_node reference to the passed in node
        self.new_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None # reference to the head
        self.tail = None # reference to the tail

    def add_to_tail(self, value):
        new_node = Node(value, None) # wrap the input value in a node

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()

        return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        
        return max_value




# ======================================================================================
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value  # value at linked list node
        self.next_node      # reference to the next node

    def get_value(self):
        return self.value

    def get_node(self):
        return self.next_node
    
    def set_next(self, new_node):
        self.next_node = new_node

class LinkedList:
    def __init__(self):
        self.head = None    # reference to the head of the list
        self.tail = None    # reference to the tail of the list


    def add_to_tail(self, value):
        
        new_node = Node(value, None) # wrap value in the input node

        # check if there is no head (i.e., the list is empty)
        if not self.head:
            self.head = new_node # set head to new node
            self.tail = new_node # set tail to new node
        
        # if the list is non-empty
        else:
            self.tail.set_node(new_node) # set the current tail's reference to new node
            self.tail = new_node         # set tails's reference to new node
    
    def remove_head(self):

        if not self.head:
            return None # return None if there is no head

        if not self.head.get_next():
            head = self.head # get a reference to the head
            self.head = None # delete the list's head reference
            self.tail = None # make sure tail doesn't refer to anything
            return head.get_value() # return th value
        value = self.head.get_value() # otherwise we have more than one element in our list
        self.head = self.head.get_next() # set the head reference to the current head's next node in the list
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head
        
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False
        
    def get_max(self):
        if not self.head:
            return None
        
        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_value()
        return max_value
        