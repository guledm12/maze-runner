#Here are the functions that the maze-runner.py program imports and utilizes.

# Function that returns a single, sample maze that you can use for testing. Maze consists of
# a 2D list of strings, each string is a wall("#"), start("O"), end("X"), or empty(" ")
def sample_maze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])
    return maze

#Return a list of all non-wall symbols surrounding the position in the maze (up/down/left/right).
def get_adjacent_positions(maze, position):

    # These poses represent up/down/left/right
    poses = [ (-1, 0), (0,1), (1, 0), (0, -1) ]
    locations = []

    # Use a loop to check each of the four possible positions
    for pose in poses:
        # Setup a new position that will represent where we need to look
        new_pose = (pose[0]+position[0], pose[1]+position[1])
        in_bounds = (-1 < new_pose[0] < len(maze[0])) and (-1 < new_pose[1] < len(maze))
        valid_spot = in_bounds and symbol_at(maze, new_pose) != "#"
        
        if in_bounds and valid_spot:
            locations.append(new_pose)

    return locations

#Returns the string in the maze, given the position.
def symbol_at(maze, position):
    return maze[position[1]][position[0]]

#Updates the maze data so that the cell at the given position is considered part of the valid path to the exit.
def add_walk_symbol(maze, position):
    maze[position[1]][position[0]] = "."

#Prints the maze in a readable way, with some spacing between each horizontal character.
def print_maze(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(maze):
            print(symbol_at(maze, (j, i)), end="   ")
        print()  