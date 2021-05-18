from node import TwoWayNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data)

        if self.count == 0:
            self.head = new_node
            self.head.next = self.head
            self.tail = self.head
        else:
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            probe.next = new_node
            new_node.next = self.head
            new_node.previous = probe
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        front = self.head

        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return front.data



if __name__ == '__main__':
    numbers = Queue()
    numbers.enqueue(1)
    numbers.enqueue(2)
    numbers.enqueue(3)
    numbers.enqueue(4)
    print(numbers.dequeue())
    print(numbers.dequeue())
    print(numbers.dequeue())
    print(numbers.dequeue())
    print()