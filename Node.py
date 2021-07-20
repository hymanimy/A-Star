import random

class Node:
    def __init__(self, r, c):
        chanceOfWall = 0.3
        self.r = r
        self.c = c
        self.gScore = float('inf')
        self.fScore = float('inf')
        self.wall = random.random() < chanceOfWall

    def get_neighbours(self, grid):
        neighbours = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)] # allows diagonals
        for i, j in dirs: 
            newR, newC = self.r + i, self.c + j
            if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid) and not grid[newR][newC].wall:
                neighbours.append(grid[newR][newC])
        return neighbours

    def __str__(self):
        return f"({self.r}, {self.c})"

    def __repr__(self):
        return f"({self.r=}, {self.c=})"



