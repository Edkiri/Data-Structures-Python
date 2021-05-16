from grid import Grid


class Cube:

    def __init__(self, edge_length):
        self.data = []
        for _ in range(edge_length):
            self.data.append(Grid(edge_length, edge_length)

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for grid in self.data:
            result += str(grid) + "\n"
        return result
