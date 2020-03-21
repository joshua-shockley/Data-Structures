from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = stack...
        self.stack = DoublyLinkedList()  # creates my instance of the dll

    def __str__(self):
        curr_node = self.stack.head
        output = ''
        output += f"{curr_node.value} <-> "
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f"{ curr_node.value} <->"
        return f" stack length: {self.size} \n the stack:{output}"

    def push(self, value):
        # utilizes the instance of dlll to add to head
        self.stack.add_to_head(value)
        # print(f"added value: {value}")
        self.size += 1  # increases the "size" to correct the count
        return f"{self.size}, {value}"

    def pop(self):
        if self.size < 1:  # my check to verify there is something to remove
            return None  # test wants to see None instead of 0 or other return
        else:
            # uses the instance to remove from top of stack
            thing = self.stack.remove_from_head()
            # print(f"removed:{thing}")
            self.size -= 1  # decreases the count so that it is accuate
            return thing  # returns the item deleted for reference

    def len(self):
        return self.size  # displays the "length" or the current count of what's added vs removed


# stack = Stack()
# stack.push(3)
# stack.push(55)
# print(stack)
# stack.pop()  # removes last push of 55
# print(stack)
# stack.push(33)
# print(stack)
# stack.push(88)
# print(stack)
