from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = stack...
        self.stack = DoublyLinkedList()  # creates my instance of the dll

    def push(self, value):
        # utilizes the instance of dlll to add to head
        self.stack.add_to_head(value)
        self.size += 1  # increases the "size" to correct the count

    def pop(self):
        if self.size < 1:  # my check to verify there is something to remove
            return None  # test wants to see None instead of 0 or other return
        else:
            # uses the instance to remove from top of stack
            thing = self.stack.remove_from_head()
            self.size -= 1  # decreases the count so that it is accuate
            return thing  # returns the item deleted for reference

    def len(self):
        return self.size  # displays the "length" or the current count of what's added vs removed
