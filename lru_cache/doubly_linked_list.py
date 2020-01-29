"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):  # sets the new pointers thus removing from list
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node  # creates the head position sets to None as default
        self.tail = node  # creates the tail position sets to None as defalut
        # sets the length method/prop to value of 0 if nothing other wise one item makes length of 1
        self.length = 1 if node is not None else 0  # done as a list comprehension

    def __len__(self):
        return self.length  # allows us to call len() as a fn

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:  # asks if there is no head and tail meaning empty
            self.head = new_node  # sets the new node to head
            self.tail = new_node  # sets the new node to be the tail also since its the only node
        else:  # meaning so if there is a length to the DLL 1 or more
            # the old head is set to the next position pointer from new node
            new_node.next = self.head
            # the new node is now set pointer that new node is prev to original head
            self.head.prev = new_node
            self.head = new_node  # sets the new node to the head position
        return new_node

    def remove_from_head(self):
        # sets the variable so it can be returned using node's value method
        value = self.head.value
        # performs the delete from below and sets the return value as self.head
        self.delete(self.head)
        return value  # actually returns the value to end the fn

    def add_to_tail(self, value):
        # creates the instance of the node
        new_node = ListNode(value, None, None)
        self.length += 1  # adds to the length prop in ListNode
        if not self.head and not self.tail:  # if list is empty
            self.head = new_node  # makes the only new value head and below tail also
            self.tail = new_node
        # this sets up the new pointer for the new last item since there  is 1+ item(s)
        else:
            new_node.prev = self.tail  # sets og tail to being the new node's now prev
            self.tail.next = new_node  # sets new nod to be the og tail's new next pointer
            self.tail = new_node  # then sets the new node to be the tail

    def remove_from_tail(self):
        value = self.tail.value  # sets the value fo the current tail to a var
        self.delete(self.tail)  # deletes the og tail
        return value  # returns the value of the deleted tail node

    def move_to_front(self, node):
        value = node.value  # sets the value of the node to move to var
        self.delete(node)  # deletes the og node (delete redoes pointers)
        self.add_to_head(value)  # adds the var value to the head position

    def move_to_end(self, node):
        value = node.value  # sets the value of the nod to move to var
        self.delete(node)  # deltes the node (delete handles pointers)
        self.add_to_tail(value)  # adds the value to tail postion

    def delete(self, node):
        self.length -= 1
        # if empty
        if not self.head and not self.tail:
            return None  # return that there is nothing
        # if head and tail
        if self.head == self.tail:
            self.head = None  # sets the value to none since there was only length=1 before delete
            self.tail = None  # same as line above but for tail
        # if the head
        elif self.head == node:  # if the lenght is more than one and deleting the head
            self.head = self.head.next  # sets the position for second item to be first
            node.delete()  # then deletes the node picked
        elif self.tail == node:  # if the lenght is more than one and deleting the tail
            self.tail = self.tail.prev  # sets the prev to tail to be new tail
            node.delete()  # deletes the og tail listNode delete fn handles the reassignement of the new prev and next
        else:
            node.delete()

    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
