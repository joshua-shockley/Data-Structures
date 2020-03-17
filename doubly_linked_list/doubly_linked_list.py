
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        output = ''
        output += f'( {curr_node.value} ) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'( {curr_node.value} ) <-> '
        return output

    """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node

    """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""

    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    # may need more done in ListNode before possible....
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""

    # may need more done in ListNode before possible....
    def move_to_end(self, node):
        pass
    """Removes a node from the list and handles cases where
                the node was the head or the tail"""

    # may need more done in ListNode before possible....
    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return 0
        if self.head == self.tail:
            value = node.value
            self.head = None
            self.tail = None
            return value
        elif self.head == node:
            self.remove_from_head()
            return node.value
        elif self.tail == node:
            self.remove_from_tail()
            return node.value
        #     #last time i did this it needed to have a delete in ListNode class to use it.. it uses the node info
        else:
            node.delete()

    """Returns the highest value currently in the list"""

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


dll = DoublyLinkedList()
dll.add_to_head(5)
dll.add_to_head(3)
dll.add_to_head(7)
dll.add_to_head(8)
dll.add_to_tail(1)

print(dll)

print(dll.get_max())
