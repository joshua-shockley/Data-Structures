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
        self.limit = limit
        self.stuff = {}
        self.length = 0
        self.dll = DoublyLinkedList()

    def __ln__(self):
        return self.length

    def __str__(self):
        return self.stuff

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        try:
            # it exists
            # value = self.stuff[key]
            # node = (key, value)
            node = self.stuff[key]
            self.dll.move_to_front(node)  # this moves to front of dll
            return node.value[1]
        except:
            # doesn't exist
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

    def set(self, key, value):  # cache is called stuff
        try:
            # It does exist
            node = self.stuff[key]
            node.value = (key, value)
            return node.value[1]
        except:
            # It does not exist
            print('makes it into: It does not exist part of set fn')
            self.length += 1
            # this is the attempt to rewire
            # this sets node for adding to dll
            node = (key, value)
            # node = self.stuff[key]
            self.dll.add_to_head(node)  # adds node to dll at the head
            self.stuff[key] = self.dll.add_to_head(
                node)  # adds key to the cache
            nv = self.stuff[key]

            while self.length > self.limit:
                tail = self.dll.tail
                key_to_go = tail.value[0]
                print('print tail', key_to_go)
                self.dll.remove_from_tail()
                # end of actually removing item past limit
                # deletes the least used value from cache
                del self.stuff[key_to_go]
                self.length -= 1
                print(self.length)

            return nv.value[1]
# this is the end of the atttempt rewire

        #     print(self.length)
        #     while self.length > self.limit:  # removes item past limit
        #         tail = self.dll.tail
        #         key_to_go = tail.value[0]
        #         print('print tail', key_to_go)
        #         self.dll.remove_from_tail()
        #         # end of actually removing item past limit
        #         # deletes the least used value from cache
        #         del self.stuff[key_to_go]
        #         self.length -= 1
        #         print(self.length)
        # finally:
        #     # this sets node for adding to dll
        #     node = (key, value)
        #     # node = self.stuff[key]
        #     self.dll.add_to_head(node)  # adds node to dll at the head
        #     self.stuff[key] = self.dll.add_to_head(
        #         node)  # adds key to the cache
        #     nv = self.stuff[key]
        #     return nv.value[1]


test = LRUCache(3)
test.set('item1', '1')
test.set('item2', '2')
test.set('item3', '3')
test.set('item2', 're-set')
print(test.get('item2'))

print(test.get('item1'))
print(test.get('item3'))
print(test.set('item4', '4'))
print('test should come back None:', test.get('item2'))
print('test should come back with value of item1:', test.get('item1'))
print(test.limit)
print(len(test.stuff))
print(test.length)
