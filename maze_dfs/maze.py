import random
import os

class Maze:
    def __init__(self, width, height):
        self.validate_dimensions(width, height)
        self.width = width if width % 2 != 0 else width + 1
        self.height = height if height % 2 != 0 else height + 1
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.start = (1,1)
        self.generate_maze(self.start[0], self.start[1])
        self.end = (self.width-2, self.height -2)
        self.maze[self.start[1]][self.start[0]] = 2
        self.maze[self.end[1]][self.end[0]] = 3  

    def validate_dimensions(self, width, height):
        if width < 2 or height < 2:
            raise ValueError("Width and height must be at least 2.")      

    def generate_maze(self, x, y):
        self.maze[y][x] = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx*2, y+dy*2
            if 0 <= nx < self.width and  0 <= ny < self.height and self.maze[ny][nx] == 1:
                self.maze[y+dy][x+dx] = 0
                self.generate_maze(nx, ny)

    def print_maze(self, path=[]):
        # print("\033[H\033[J", end='')
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                    
                if self.maze[y][x] == 1:
                    print("█", end="")
                elif (x,y) in path:
                    print("X", end="")
                elif self.maze[y][x] == 2:
                    print("S", end="")
                elif self.maze[y][x] == 3:
                    print("E", end="")
                else:
                    print(" ", end="")
            print()

