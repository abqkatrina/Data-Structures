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
        #make the value a node
        new_node = ListNode(value)
        #adding to the list adds to the length
        self.length += 1
        #if there's no head make it (it's also the tail)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            #move the head value down a node
            new_node.next = self.head
            # make the old head not a head
            self.head.prev = new_node
            #define the new head
            self.head = new_node
            
 
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    #WORKS
    def remove_from_head(self):
        if self.head is None:
            print("Empty List")
            return
        head_val = self.head.value
        self.delete(self.head)
        return head_val
  
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    #WORKS
    def add_to_tail(self, value):
        #make the value a node
        new_node = ListNode(value)
        #adding to the list adds to the length
        self.length += 1
        #if there's no tail, make one (it's also the head)
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            #move the tail value back a node
            new_node.prev = self.tail
            #make the old tail not a tail
            self.tail.next = new_node
            #define the new tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    #WORKS     
    def remove_from_tail(self):
        #>>No list
        if self.head is None:
            print("Empty List")
            return
        tail_val = self.tail.value
        self.delete(self.tail)
        return tail_val
        
         
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
    #WORKS
    def move_to_front(self, node):
        #if it's at the fron, you're done
        if node is self.head:
            return
        #make the value the new head
        self.add_to_head(node.value)
        #remove it from where it was
        self.delete(node)
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    #WORKS
    def move_to_end(self, node):
       #if it's at the end, you're done
        if node is self.tail:
            return
        #make the value a new tail
        self.add_to_tail(node.value)
        #remove value from wherever it was
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    #WOR
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
        #start at head -- going to loop, so make a temp
        cur_node = self.head

        #make a max to compare to
        max = self.head.value

        #look at all the values -- loop
        while cur_node:
            #if the current value is bigger than the original, set that to max
            if cur_node.value > max:
                max = cur_node.value
            #if not, move on to the next value and compare it to max
            cur_node = cur_node.next
        return max


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
