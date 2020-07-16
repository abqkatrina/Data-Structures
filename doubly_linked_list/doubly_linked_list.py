"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    #WORKS
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            cur_node = self.head
            self.head = new_node
            self.head.next = cur_node
            self.head.prev = None
 
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
#NOT WORKING
    def remove_from_head(self):
        cur_node = self.head
        if cur_node is None:
            print("Empty List")
        if cur_node.next is None:
            cur_node = None
        cur_node = cur_node.next
        cur_node.prev = None 
        self.length -= 1  
  
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    #WORKS
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
#NOT WORKING     
    #prev_node.next = None
    # AttributeError: 'NoneType' object has no attribute 'next'
    def remove_from_tail(self):
        #>>No list
        if self.head is None:
            print("Empty List")
            return

        #>> If head is tail, delete head
        if self.head.next is None:
            self.head = None
            return

        #>> While not tail, keep going
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        prev_node = cur_node.prev
        prev_node.next = None
        cur_node = None
         
    #WORKS
    def contains(self, value):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.value == value:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False

    #WORKS        
    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
#NOT WORKING self.head.prev = None int object has no attribute prev
    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            cur_node = node
            self.head.next = self.head
            self.head = cur_node
            self.head.prev = None
            cur_node = None
            return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
#NOT WORKINGself.tail.next = None  int object has no attribute next
    def move_to_end(self, node):
        cur_node = node
        if cur_node is self.tail:
            return
        else:
            self.tail.prev = self.tail
            self.tail = cur_node
            self.tail.next = None
            cur_node = None
            return

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
 #NOT WORKING attribute error int object has no attribute delete
    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    #WORKS
    def get_max(self):
        maxtotal = 0
        if self.head is None:
            maxtotal = 0
        cur_node = self.head
        while cur_node is not None:
            maxtotal += cur_node.value
            cur_node = cur_node.next
        print(maxtotal)

    #WORKS
    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node is not None:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node =  next
        self.head = prev
       
            

dll = DoublyLinkedList()
dll.add_to_head(2)
dll.add_to_head(1)
dll.add_to_tail(3)
dll.add_to_tail(4)
dll.add_to_tail(77)

# dll.remove_from_head() -- doesn't delete but no error....
# dll.remove_from_tail() -- doesn't delete, attr error

# dll.move_to_front(3) -- doesn't work, attr error
# dll.move_to_end(3) -- doesn't work, attr error

# dll.contains(3) OK
# dll.get_max() OK
# dll.reverse() OK
# dll.delete(77) -- delete doesn't work (attr error)
dll.printlist()
