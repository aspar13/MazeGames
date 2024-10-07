import time 
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        path = []
        self.dfs(self.maze.start[0], self.maze.start[1], path)
        # return path
    
    def dfs(self, x, y, path):
        if (x,y) == self.maze.end:
            return True 
        
        if 0 <= x < self.maze.width and 0 <= y <self.maze.height and self.maze.maze[y][x] != 1 and (x, y) not in path:
            path.append((x,y))
            time.sleep(0.1)
            self.maze.print_maze(path)

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if self.dfs(x + dx, y + dy, path):
                    return True 
                
            path.pop()
            self.maze.print_maze(path)
            time.sleep(0.1)
        return False
    


