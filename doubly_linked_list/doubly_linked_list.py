"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self, node):
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
        if self.head == 0:
            return 0
        count = 0
        while self.head:
            count += 1
            self.head = self.head.next
        return count
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    WORKS
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        cur_node = self.head
        if cur_node is None:
            print("Empty List")
        else:
            self.length -= 1
            print(cur_node.value)
            print(self.length)
            self.delete(self.head)
            cur_node = None       

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    WORKS
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        cur_node = self.tail
        if cur_node is None:
            print("Empty List")
        else:
            return cur_node.value
            cur_node = cur_node.next
            cur_node.next = None
            print(self.length)
        


    def contains(self, value):
        cur_node = self.head
        if cur_node.value is None:
            print("Empty List")
            return
        else:
            while cur_node.value is not None:
                if cur_node.value == value:
                    return True
                    cur_node = cur_node.next
                else:
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
    def move_to_front(self, node):
        cur_node = node
        if cur_node is self.head:
            return
        if cur_node is self.tail.value:
            self.remove_from_tail()
        self.add_to_head(cur_node)
        # NEED TO DELETE NODE FROM PREVIOUS SPOT
        self.length -= 1
        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        cur_node = node
        if node is self.tail:
            return
        if node is self.head:
                self.remove_from_head()
        else:
            self.delete(cur_node) # 'int' has no attribute 'delete'
            self.length -= 1
        self.add_to_tail(cur_node)



    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -= 1
        if self.head is self.tail:
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
    def get_max(self):
        max_value = []
        if self.head:
            max_value.append(self.value)
            if self.right:
                max_value.append(self.value + self.right.value)
            else:
                return max_value
        else:
            return 0
            

dll = DoublyLinkedList()
dll.add_to_head(2)
dll.add_to_head(1)
dll.add_to_tail(3)
dll.add_to_tail(4)
# dll.printlist()
# dll.remove_from_head()
# dll.remove_from_tail

# dll.move_to_front(3)
# dll.move_to_end(3)
# dll.contains(3)
dll.printlist()
