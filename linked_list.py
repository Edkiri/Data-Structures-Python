from node import Node
from arrays import Array

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
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
        return str(self.size)

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

            
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!!")

    
    def clear(self):
        self.head = None
        self.size = 0

    
    def add_array(self, array):
        """
        Append the elemets of an 'array'
        into the SinglyLinkedList instance as Nodes.
        """
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