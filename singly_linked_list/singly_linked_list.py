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
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')
        return "-->".join(nodes)

    def append_node(self, value)
        node = Node(value)
        if self.head:
                self.head.next = node
                self.head = node
        else:
            self.tail = node
            self.head = node

    def pop_node(self, value)
        current = self.tail
        prev = self.tail
        while current:
            if current.value == value:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


