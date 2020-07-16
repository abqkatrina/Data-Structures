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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_value = value
        if self.value:
            if new_value <= self.value:
                if self.left is None:
                    self.left = BSTNode(new_value)
                else:
                    self.left.insert(new_value)
            if new_value >= self.value:
                if self.right is None:
                    self.right = BSTNode(new_value)
                else:
                    self.right.insert(new_value)
            if new_value == self.value:
                print("Equal")

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if current node equals target value
        if self.value == target:
            return True
        #if target is larger than current node, move right
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)
        #if target is smaller than current node, move left
        if self.value > target:
            if self.left is None:
                return False
            return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        #if root is only value:
        if self.right is None:
            return self.value
        return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #print nothing if there is no current value
        if node is None:
                return

        #if left exists, move left & print
        if node.left:
            node.left.in_order_print(node.left)

        #print current value
        print(node.value)

        #if right exists, move right & print
        if node.right:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal (queue, level order)
    def bft_print(self, node):
        #print nothing if there is no current value
        if node is None:
            return

        #print all values in tree, level by level, from top level l->r to bottom level l->r

        #make a Queue
        queue = []
        #add starting point
        queue.append(node)

        #make a loop through the tree, printing and popping so long as queue is not empty
        while (len(queue) > 0):
            #print the first in line
            print(queue[0].value)
            node = queue.pop(0)

            #now add left of next layer
            if node.left:
                queue.append(node.left)

            #now add right of next layer
            if node.right:
                queue.append(node.right)
        #it will print , pop, and look left then right again at next level



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (queue, left root right)
    def dft_print(self, node):
        #if tree is empty
        if node is None:
            return
        
        #make a queue
        queue = []
        #add a starting point
        queue.append(node)

        #loop so long as there's something in the queue
        while(len(queue) > 0):
                #print the first in line and pop it
                node = queue.pop()
                print(node.value)

                #first, go all the way left
                if node.left:
                    queue.append(node.left)

                #go all the way right
                if node.right:
                    queue.append(node.right)

                  

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT -- self, left, right (all lefts to end, then all rights FROM end)
    #print(self) first
    def pre_order_dft(self, node):
        if node is None:
            return
        #print current value
        print(node.value)
        #if left exists, move left & print
        if node.left:
            node.left.in_order_print(node.left)
        #if right exists, move right & print
        if node.right:
            node.right.in_order_print(node.right)

    # Print Post-order recursive DFT -- left, right, self (last level (starting left end) to top level(self))
    #print(self) last
    def post_order_dft(self, node):
        if node is None:
            return
        #if left exists, move left & print
        if node.left:
            node.left.in_order_print(node.left)
        #if right exists, move right & print
        if node.right:
            node.right.in_order_print(node.right)
        #print current value
        print(node.value)
