# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:  # checks for input value with value stored in init?
            if not self.left:  # if not self.left make one
                self.left = BinarySearchTree(value)  # makes the node/tree
            # recursion below
            else:
                self.left.insert(value)
        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:  # set so that if the target/input is less that it compares either a value or None
            if self.left is None:  # if a self.value/node is assigned to None making it a leaf
                return False  # returns False since the node/self.left is empty
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        if target == self.value:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
