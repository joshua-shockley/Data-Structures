

from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        # this is making the instance of the dll for stroage to use below
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        # use the storage/queue made above to get started and then the imported method to add/remove
        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size < 1:
            return None
        else:
            # sets the value to be returned of what is deleted/removed then also performs the function
            thing = self.queue.remove_from_head()
            self.size -= 1  # makes sense to do this after checks out
            return thing

    def len(self):

        return self.size
