from node import Node
from arrays import Array

class SinglyLinkedList:

    def __init__(self):
        """ initializes a empty list. """

        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """ Add a node into de LinkedList with the data. """

        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.tail = node

        self.size += 1

    
    def size(self):
        """ Returns the size of the list. """
        return str(self.size)

    def iter(self):
        """ Iterates through each of the node values in the list. """

        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

            
    def search(self, data):
        """ Ensures that 'data' is on the list or not. """
        
        for node in self.iter():
            if data == node:
                print(f"Data {data} has been found!!")
            else:
                print(f"Data {data} has not been found.")


    
    def clear(self):
        """ Empty the list. """

        self.head = None
        self.size = 0

    
    def add_array(self, array):
        """Append the elemets of an Array into the list  as Nodes."""

        for element in array:
            node = Node(element)

            if self.head == None:
                self.head = node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = node
                
            self.size += 1


if __name__ == '__main__':

    linked_list = SinglyLinkedList()
    for i in range(1,6):
        linked_list.append(i)