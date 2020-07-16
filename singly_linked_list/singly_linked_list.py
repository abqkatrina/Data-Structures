class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
            return self.value

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None

#WORKS
    def printlist(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.value)
            cur_node = cur_node.next
        
#WORKS        
    def add_to_head(self, value):
        #make the value a node
        new_node = Node(value)
        #if list is empty, make new node head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #if list is not empty, make new node the head
        #move the old head to next
        new_node.next = self.head
        #set the head to new node
        self.head = new_node
        return

#WORKS 
    def add_to_tail(self, value):
        #make the value a node
        new_node = Node(value)
        #if list is empty, make new node the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #if list is not empty, make new node the tail
        #make old tail to prev
        self.tail.next = new_node
        #set the tail to new node
        self.tail = new_node

#WORKS
    def insert_node_after(self, prev_node, value):
        if not prev_node:
            print("No prev_node")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

#WORKS 
    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False

#WORKS
    def listlength(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        print(count)

#WORKS 
    def remove_head(self):
        #if list is empty...
        if self.head is None:
            return None
        head_val = self.head.value
        #if head is tail...
        if self.head.next is None:
            self.head = None
            self.tail = None
            return head_val
        #if list is full..
        #make the old head the next in line
        self.head = self.head.next
        return head_val
        

#WORKS
    def remove_tail(self):
        cur_node = self.head
        if cur_node is None:
            return("No self.tail")
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None
        
#WORKS
    def remove_node_at(self, pos):

        cur_node = self.head
        if cur_node is None:
            print('Empty List')
            return
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        for i in range(pos -1):
            cur_node = cur_node.next
            if cur_node is None:
                break
        next = cur_node.next.next
        cur_node.next = None
        cur_node.next = next

#WORKS
    def get_max(self):
        #if list is empty ...
        if self.head is None:
            return None
        #make a max to compare to -- start at head
        max = self.head.value
        #need to loop -- make a temp start at next value
        cur_node = self.head.next
        #check every value
        while cur_node is not None:
            #if the current value is bigger than max, make it max
            if cur_node.value > max:
                max = cur_node.value
            #if not, move on to the next node
            cur_node = cur_node.next
        return max


        
            
        


# ll = LinkedList()
# ll.add_to_head(5)
# ll.add_to_head('seventeen')

# ll.insert_node_after(ll.head, 84.9)

# ll.add_to_head("A")
# ll.add_to_tail("Z")
# ll.printlist()
# ll.remove_node_at(1)
# # ll.printlist()
# ll.remove_head()
# ll.remove_tail()
# # ll.printlist()
# ll.contains("A")
# ll.printlist()
# ll.listlength()

