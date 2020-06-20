class ListNode:

    def __init__(self, item = None, link = None):
        """
        create a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link
        """
        self.item = item
        self.link = link

    def get_item(self):
        """ returns the data element stored at the node
        pre: none
        post: returns the data element stored at the node """
        return self.item

    def get_link(self):
        """ returns the next link stored at the node
        pre: none
        post: returns the next link stored at the node """
        return self.link

    def set_link(self, link):
        """ returns the next link stored at the node
        pre: none
        post: sets the next link stored at the node to link """
        self.link = link

class LList:
    
    def __init__(self, seq=()):
        
        """ creates an LLis
        post: Creates an LList containing items in seq """

        self.head = None
        self.size = 0

        # if passed a sequence, place items in the list
        for x in seq:
            self.append(x)

    def __len__(self):
        """post: returns number of items in the list """
        return self.size

    def _find(self, position):
        """ private method that returns node that is at location position
        in the list (0 is first item, size=1 is last item)
        pre: 0 <= position < self.size
        postL returns the ListNode at the specified position in the list
         """

        assert 0 <= position < self.size

        node = self.head

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link

        return node

    def append(self, x):
        """ appends x onto end of the list
        post: x is appended onto the end of the list """

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1
        