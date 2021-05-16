from functools import reduce
import random as rd
import string


class Array:

    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __fill__(self, min_n=0, max_n=10):
        
        for i in range(len(self.items)):
            if rd.randint(0,1) == 1:
                self.items[i] = rd.randint(min_n, max_n)
            else:
                self.items[i] = rd.choice(string.ascii_letters)

    def __sum_items__(self):

        nums = list(filter(lambda a: type(a) is int, self.items))
        chars = list(filter(lambda a: type(a) is str, self.items))

        final = f"{reduce(lambda a,b: a + b, nums)} {reduce(lambda a,b: a + b, chars)}"

        return final