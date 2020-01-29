from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.order = DoublyLinkedList()
        self.storage = dict()
        self.size = 0
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None
        # try:
        #     # it exists
        #     node = self.storage[key]
        #     print(node.value[0], node.value[1])
        #     self.order.move_to_front(node)  # this moves to front of dll
        #     return node.value[1]
        # except:
        #     # doesn't exist
        #     return None
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

    def set(self, key, value):  # cache is called stuff
        # if already exist, overwrite value
        if key in self.storage:
            # update dict aka stuff
            node = self.storage[key]
            node.value = (key, value)
            # mark as most recently used - put in head of DLL
            self.order.move_to_front(node)
            return
        # if at max capacity, dump oldest-remove from tail of DLL
        if self.size == self.limit:
            # dump oldest
            # remove from cache stuff
            del self.storage[self.order.tail.value[0]]
            # remove from dll
            self.order.remove_from_tail()
            self.size -= 1
        # add pair to the cache -add to dict and add it nodes/DLL
        node = (key, value)
        self.order.add_to_head(node)
        self.storage[key] = self.order.head
        self.size += 1

        # try:
        #     # It does exist
        #     node = self.stuff[key]
        #     node.value = (key, value)
        #     self.dll.move_to_front(node)  # this moves to front of dll
        #     return node.value[1]
        # except:
        #     # It does not exist
        #     print('makes it into: It does not exist part of set fn')
        #     self.length += 1
        #     # this is the attempt to rewire
        #     # this sets node for adding to dll
        #     node = (key, value)
        #     self.dll.add_to_head(node)  # adds node to dll at the head
        #     self.stuff[key] = self.dll.add_to_head(
        #         node)  # adds key to the cache
        #     nv = self.stuff[key]

        #     if self.length == self.limit+1:
        #         tail = self.dll.tail
        #         key_to_go = tail.value[0]
        #         print('print tail', key_to_go)
        #         self.dll.remove_from_tail()
        #         # end of actually removing item past limit
        #         # deletes the least used value from cache
        #         del self.stuff[key_to_go]
        #         self.length -= 1
        #         print(self.length)

        #     return nv.value[1]


test = LRUCache(2)
test.set('item1', '1')
test.set('item2', '2')


print(test.get('item1'))
print(test.set('item4', '4'))
print('test should come back None:', test.get('item2'))
print('test should come back with value of item1:', test.get('item1'))
print('limit', test.limit)
print('dll len', len(test.order))
print('test length:', test.size)
print(str(test.order))
