class Human:
    def __init__(self, maze):
        self.maze = maze

                
    def play(self):
        x,y = self.maze.start
        path = [(x,y)]

        while (x,y) != self.maze.end:
            self.maze.print_maze(path)
            move = input("Enter move (w/a/s/d): ").lower()
            dx, dy = {
                        "w": (0, -1),
                        "a": (-1, 0),
                        "s": (0, 1),
                        "d": (1, 0)
                    }.get(move, (0,0))
            
            nx, ny = x+dx, y+dy

            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and self.maze.maze[ny][nx] != 1:
                if (nx, ny) in path:
                    index = path.index((nx,ny))
                    path = path[:index + 1]
                else:
                    path.append((nx, ny))
                x, y = nx, ny
        self.maze.print_maze(path)
        print("Congratulations! You solved the maze!")
        

