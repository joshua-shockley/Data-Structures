

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

    def __str__(self):
        if self.queue.head is None and self.queue.tail is None:
            return None
        curr_node = self.queue.head
        output = ''
        output += f"{curr_node.value}\n"
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f"{curr_node.value}\n"
        return output

    def enqueue(self, value):
        # use the storage/queue made above to get started and then the imported method to add/remove
        self.queue.add_to_tail(value)
        # print(f"added : {value}")
        self.size += 1

    def dequeue(self):
        if self.size < 1:
            return None
        else:
            # sets the value to be returned of what is deleted/removed then also performs the function
            thing = self.queue.remove_from_head()
            # print(f"{thing}")
            self.size -= 1  # makes sense to do this after checks out
            return thing

    def len(self):

        return self.size


# q = Queue()
# q.enqueue(4)
# print(q)
# q.enqueue(54)
# q.enqueue(3)
# print(q)
# q.dequeue()
# print(q)
