class Node:
    def __init__(self, data):
        self.data = data  # The data value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head node to None
        self.tail = None  # Initialize the tail node to None

        

    # Method to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            self.tail = new_node  # Set the new node as the tail
        else:
            self.tail.next = new_node  # Set the new node after the current tail
            new_node.prev = self.tail  # Set the current tail as the previous node for the new node
            self.tail = new_node  # Update the tail to the new node



    # Method to display the list from head to tail
    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    # Method to display the list from tail to head
    def display_backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        return elements
    


dll = DoublyLinkedList()

dll.append("maine")
dll.append("New Hampshire")
dll.append("Massachusetts")
dll.append("Rhode Island")
dll.append("Connecticut")


print(dll.display_forward())
print(dll.display_backward())