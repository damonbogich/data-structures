"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue2 import Queue
from queue2 import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #case 1: value is less than self.value
        if value < self.value:
            #if no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        #case 2: value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #case 1: self.value is = target
        if self.value == target:
            return True
        #case 2: if target is < self.value
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        #case 3: if target is >= self.value
        else:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #will be recursive
        fn(self.value)
        if self.right is None and self.left is None:
            return
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:
            return
        #check if we can move left
        if self.left is not None:
            self.left.in_order_print(node)
        
        #visit the node by printing it's value
        print(self.value)

        if self.right is not None:
            self.right.in_order_print(node)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    #how do i get a queue in here?
    def bft_print(self, node):
        
        #use a queue to form a line
        #for the nodes to get in
        my_queue = Queue()
        
        #start by placing the root in queue
        current_node = self
        my_queue.enqueue(current_node)
        #need a while loop to iterate
        #while length of queue is > 0:
        while my_queue.size > 0:
            #dequeue item from front of queue
            #print that item
            current_node = my_queue.storage[0]
            my_queue.dequeue()
            print(current_node.value) #need this to be item dequeued
            #place current item's left node in queue if not none
            if current_node.left is not None:
                my_queue.enqueue(current_node.left)
            #place current item's right node in queue if not none
            if current_node.right is not None:
                my_queue.enqueue(current_node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal(not recursive)
    def dft_print(self, node):
        
        #initialize an empty stack
        #Push root node onto stack
        my_stack = Stack()
        current_node = self
        my_stack.push(current_node)
        #need a while loop to manage our iteration 
        while my_stack.size > 0:
        #If size of stack > 0 enter while loop:
            #pop top item off of stack 
            #print that item's value
            current_node = my_stack.storage[0]
            my_stack.pop()
            print(current_node.value)

        
            #if there is a right sub tree:
                #push right item onto stack 
                #(pushing right on first ensures that left is printed first...LIFO)
            if current_node.right is not None:
                my_stack.push(current_node.right)
            #if there is a left sub tree:
                #push left item onto stack
            if current_node.left is not None:
                my_stack.push(current_node.left)

            




    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
