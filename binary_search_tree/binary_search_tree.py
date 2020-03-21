from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')
# must be in this directory for the import to work


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # so upon the initial creation this has a value of None so when first made it has a larger value?
        if value < self.value:  # here this compares what was in the init for the original root value with the to be inserted one
            if not self.left:  # starting comparison
                # makes the node if smaller
                # creates new tree which is its own tree also in the location determined by the camparison
                self.left = BinarySearchTree(value)
            else:
                # this recurses if there is a left
                # this keep looking for where it belongs if there are already values/nodes in tree
                return self.left.insert(value)
        if value >= self.value:  # repeated same as the left above
            if not self.right:
                self.right = BinarySearchTree(
                    value)  # makes the node if bigger
            else:
                # this recurses if there is a right
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:  # this starts at the root node and then we work our way down
            # if its smaller and nothing there to compare it isnt in there (base case)
            if self.left is None:
                return False
            else:
                # creates the recursive move to the left
                return self.left.contains(target)
        if target > self.value:
            # if target is larger but there isnt a right to compare then it isnt in there (base case)
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target == self.value:  # this is our base case so this is where we return True once found
            return True

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # STILL WORKING ON THIS PART.. KEEPS THROWING OUT NEW ERRORS EACH TIME I ADJUST ANYTHING
    def for_each(self, cb):
        curr_node = self.value
        print(curr_node)
        cb(curr_node)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # else:
        #     return cb(curr_node)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):  # prints None at the end but passes, why?
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)
        # elif node.left is None and node.right is None:
        #     pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):  # works at each height
        # create a queue for nodes
        q = Queue()
        # add current node to queue
        q.enqueue(node)
        # while the queue isn't empty
        while q.len() > 0:
            # dequeue a node
            # print the dequeued node
            # print("q:", q)
            # it was wrong when assigning a new variable name instead of reassigning the new value to existing node
            # ex: thing=.....
            node = q.dequeue()
            print(node.value)
            # add it's chldren to queue
            # i.e add left (if can)
            if node.left is not None:
                # lvalue = self.left.value
                # print("entered left value:", lvalue)
                q.enqueue(node.left)
            # add right (if can)
            if node.right is not None:
                # rvalue = self.right.value
                # print("entered right value:", rvalue)
                q.enqueue(node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        # create a stack
        stack = Stack()
        # push the current node onto stack
        stack.push(node)
        # while we have items on stack
        while stack.size > 0:
            # print current value and then pop it off
            node = stack.pop()
            # now that i have assigned the return from the pop a variable name print what was popped
            print(node.value)
            # push the right value of the current node (if can)
            if node.right is not None:
                stack.push(node.right)
            # push the left value of current node (if can)
            if node.left is not None:
                stack.push(node.left)
        # pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print pre-order recursive DFT

    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # backwords print
        if node == None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)


tree = BinarySearchTree(5)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(6)
tree.insert(8)
# tree.in_order_print(tree)

# arr = []

# def bb(x): return arr.append(x+1)

# tree.for_each(bb)
# print(arr)
print("bft_print")
tree.bft_print(tree)
print("dft_print")
tree.dft_print(tree)
print("pre_order")
tree.pre_order_dft(tree)
print("post_order")
tree.post_order_dft(tree)
