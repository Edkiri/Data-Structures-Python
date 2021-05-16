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
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
            self.tail = node

        self.size += 1

    
    def size(self):
        """ Returns the size of the list. """
        return str(self.size)

    def iter(self):
        """ Iterates through each of the node values in the list. """

        probe = self.head
        while probe:
            val = probe.data
            probe = probe.next
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
                probe = self.head
                while probe.next:
                    probe = probe.next
                probe.next = node
                
            self.size += 1

    def replace(self, target_item, new_data):
        """ 
        Replaces the node with the value "target_item" with 
        a new node with a value of "new_data". 
        """
        new_node = Node(new_data)

        probe = self.head
        previus = self.head
        counter = 0
        while probe.next != None and probe.data != target_item:
            probe = probe.next
            if counter > 0:
                previus = previus.next
            counter += 1
        if probe.data == target_item and probe == self.head:
            new_node.next = probe.next
            self.head = new_node
        elif probe.data == target_item:
            new_node.next = probe.next
            previus.next = new_node
        else:
            print("The target item is not in the list.")
            


if __name__ == '__main__':

    linked_list = SinglyLinkedList()
    for i in range(1,5):
        linked_list.append(i)

    for el in linked_list.iter():
        print(el)