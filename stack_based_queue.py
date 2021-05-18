

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, item):
        self.inbound_stack.append(item)

    def dequeue(self):
        if self.inbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()


if __name__ == '__main__':
    numbers = Queue()
    numbers.enqueue(5)
    numbers.enqueue(6)
    numbers.enqueue(7)
    print(numbers.inbound_stack, numbers.outbound_stack)
    print(numbers.dequeue())
    print(numbers.inbound_stack, numbers.outbound_stack)
    print(numbers.dequeue())
    print(numbers.inbound_stack, numbers.outbound_stack)
