from dll_stack import Stack
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

sys.path.append('../dll_stack.py')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=4):
        self.limit = limit
        # the entire node is stored in dict as Key:tuple= (key,value)
        self.storage = {}
        self.size = 0
        self.dll = DoublyLinkedList()  # the node is storing the value

    def __str__(self):
        curr_node = self.dll.head
        output = ""
        output += f"{curr_node.value} <-> "
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f"{curr_node.value} <-> "
        return f" lru size: {self.size} \n Nodes: {output}"

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):  # cache is called storage
        if key in self.storage:
            node = self.storage[key]
        # if key in storage:
        #   move it to head
        #   return the value
            print(self.storage)
            self.dll.move_to_front(node)

            return node.value[1]  # as a tuple this key is [0] and value is [1]
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):  # cache is called storage
        # check for key in dict aka storage:
        if key in self.storage:
            # if is in storage:
            node = self.storage[key]  # grabbing the entire node stored in dict
            # update it with new info
            # creates the tuple that holds the data for the node stored in the dict
            node.value = (key, value)

            # move to position of most recently used (head)
            self.dll.move_to_front(node)

            # nothing else to do to return and exit
            return
        else:
            # if full:
            if self.size == self.limit:
                # remove least recently used  item (tail) from  dll
                self.dll.remove_from_tail()
                # remove from dict
                del self.storage[self.dll.tail.value[0]]
                # reduce size
                self.size -= 1
            self.dll.add_to_head((key, value))
        # we set it to list (key, value) as a node
        # we need to set to the cache/dict
            self.storage[key] = self.dll.head
        # we need to add to size
            self.size += 1
        return


cache = LRUCache()
print(cache.size)
cache.set(1, 55)
print(cache)
print("geting what isn't made yet: ", cache.get(2))
cache.set(2, 35)
cache.set(3, 44)
print("get 3:", cache.get(3))
print(cache)

print("get 1:", cache.get(1))
print(cache)
print(cache.set(1, 'new'))
print(cache)

print("get 2:", cache.get(2))
print(cache)

print("setting 4: ", cache.set(4, 22))
print(cache)

print("setting 5 (this should remove key3):", cache.set(5, 100))
print(cache.limit)
print(cache)
