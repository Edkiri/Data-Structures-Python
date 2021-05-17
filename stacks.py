from node import Node
from arrays import Array

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1


    def pop(self):
        
        if self.size > 0:

            data = self.top.data
            self.top = self.top.next

            self.size -= 1

            return data
        else:
            return "The stack is empty"

    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    
    def clear(self):
        self.top = None
        self.size = 0

    
    def iter(self):
        probe = self.top
        while probe != None:
            data = probe.data
            probe = probe.next
            yield data

    
    def __contains__(self, item):
        probe = self.top
        while probe != None and probe.data != item:
            probe = probe.next

        if probe and probe.data == item:
            return True
        else:
            return False
            


class ArrayStack(Array):
    def __init__(self, capacity, fill_value=None):
        Array.__init__(self, capacity, fill_value)
        self.top_index = self.__len__() - 1
        self.size = 0

    def iter(self):
        for elm in filter(lambda x: x != None, self.items):
            yield elm

    def push(self, data):
        if self.top_index == 0:
            print("The stack is full")
        else:
            if not self.items[self.top_index]:
                self.items[self.top_index] = data
            else:
                self.top_index -= 1
                self.items[self.top_index] = data
            self.size += 1

    
    def pop(self):
        if self.size > 0:
            val = self.items[self.top_index]
            self.items[self.top_index] = None
            self.top_index += 1
            self.size -= 1
            return val
        else:
            return "The stack is empty"

    
if __name__ == '__main__':
    food = ArrayStack(5)
    food.push("egg")
    food.push("ham")
    food.push("bacon")
    food.push("milk")
    food.push("pepper")
    food.push("cucumber")

    for _ in range(food.__len__()+1):
        print(food.pop())

    # print(food.__contains__("egg"))
    # print(food.__contains__("milk"))
    # food.clear()
    # for elm in food.iter():
    #     print(elm)

    print()