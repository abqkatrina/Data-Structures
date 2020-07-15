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

    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
        
    def add_to_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
                self.head = new_node
                return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_node_after(self, prev_node, value):
        if not prev_node:
            print("No prev_node")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def contains(self, value):
        cur_node = self.head
        node_id = 1
        results = []
        
        while cur_node is not None:
            if cur_node.value == value:
                results.append(node_id)
            cur_node = cur_node.next
            node_id = node_id + 1
        
        print(results)

    def listlength(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count


    def remove_head(self):
        cur_node = self.head
        if cur_node is None:
            return("No self.head")
        else:
            self.head = cur_node.next
            cur_node = None

    def remove_tail(self):
        cur_node = self.tail
        if cur_node is None:
            return("No self.tail")
        else:
            cur_node = None
        

    def remove_node_at(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        count = 1
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None


ll = LinkedList()
ll.add_to_head(5)
ll.add_to_head('seventeen')

ll.insert_node_after(ll.head, 84.9)

ll.add_to_head("A")
ll.add_to_tail("Z")
# ll.printlist()
ll.remove_node_at(3)
# ll.printlist()
ll.remove_head()
# ll.printlist()
ll.contains("A")
ll.printlist()
ll.add_to_head("A")
ll.add_to_tail("Z")
ll.printlist()
ll.contains("A")


