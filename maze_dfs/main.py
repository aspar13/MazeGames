from maze import Maze
from mazeSolver import MazeSolver 
from player import Human

def main():
    maze = Maze(13, 13)

    print("1. Play the maze game")
    print("2. Watch AI aolve the maze game")
    choice = input("Enter your choice (1 | 2): ")

    if choice == "1":
        human = Human(maze)
        human.play()
    elif choice == "2":
        solver = MazeSolver(maze)
        solver.solve()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()