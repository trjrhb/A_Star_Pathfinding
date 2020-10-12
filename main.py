"""
What is A* Search Algorithm?
A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

Why A* Search Algorithm?
Informally speaking, A* Search algorithms, unlike other traversal techniques,
it has “brains”. What it means is that it is really a smart algorithm which separates it from the other conventional 
algorithms. This fact is cleared in detail in below sections. And it is also worth mentioning that many games and 
web-based maps use this algorithm to find the shortest path very efficiently (approximation). 
"""

UNBLOCKED_CELL = 0
BLOCKED_CELL = 1
START_POINT = 2
DESTINATION = 3


class Graph:
    def __init__(self, width, height, start, dest):
        self.width = width
        self.height = height
        self.start = start
        self.dest = dest
        self.grid = [[Cell(row, column, UNBLOCKED_CELL) for column in range(height)] for row in range(width)]
        self.grid[start[0]][start[1]].value = START_POINT
        self.grid[dest[0]][dest[1]].value = DESTINATION

    def __repr__(self):
        for row in range(self.width):
            for col in range(self.height):
                print(self.grid[row][col].value, end=" ")
            print('')
        return '\n'


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def get_value(self):
        return str(self.value)


def main():
    start = [0, 0]
    destination = [5, 4]

    graph = Graph(6, 5, start, destination)
    print(graph)


main()
