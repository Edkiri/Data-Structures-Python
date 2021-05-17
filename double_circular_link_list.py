from node import TwoWayNode

class DoubleCircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def append(self, data):
        node = TwoWayNode(data)
        if self.head == None:
            self.head = node
            self.head.next = self.head
            self.tail = self.head
            self.size += 1
        else:
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            probe.next = node
            node.next = self.head
            node.previous = probe
            self.tail = node
            self.size += 1

    
    def inverse_iter(self):
        probe = self.tail
        while probe != None:
            val = probe.data
            probe = probe.previous
            yield val


    def iter(self):
        probe = self.head
        size = self.size
        while size > 0:
            val = probe.data
            probe = probe.next
            size -= 1
            yield val

    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


    def delete(self, data):
        probe = self.tail
        while probe.previous != None and probe.data != data:
            probe = probe.previous
        if probe.data == data and self.head == self.tail:
            self.clear()
        elif probe.data == data:
            if probe == self.tail:
                self.tail = probe.previous
            probe.previous.next = probe.next
            if probe.next != self.head:
                probe.next.previous = probe.previous
            self.size -= 1


if __name__ == '__main__':

    dcl_list = DoubleCircularLinkedList()
    dcl_list.append(1)
    dcl_list.append(2)
    dcl_list.append(3)
    dcl_list.append(4)
    dcl_list.delete(2)
    dcl_list.delete(4)
    dcl_list.delete(3)
    dcl_list.delete(1)

    for elm in dcl_list.iter():
        print(elm)
    print()

    

