from maze_helper import *

def dfs(maze,position,explored):                                    #Function that performs a depth-first-search on a maze.
    adjacents = get_adjacent_positions(maze,position)               #Find adjacent positions to the single specified position.

    while True:
        for adj in adjacents:                                       #Iterates over every adjacent position.
            if (adj in explored) == False:                          #If statement that determines if we have already explored this position.
                explored.append(adj)                                #Appends this position to our list of explored points.

                if symbol_at(maze,adj) == "X":                      #If statement that determines if we've reached the end of the maze.
                    for point in explored:                 
                        add_walk_symbol(maze,point)                 #Draws every point from our list of explored points. (Essentially draws out the path we took.)
                    print_maze(maze)
                else:
                    dfs(maze,adj,explored)                          #Calls DFS again in a recursive manner for the adjacent position.
                                                                    
        if position in explored:                                    #If program reaches here, it means we've reached a dead end.
            explored.remove(position)                               #Removes the path to the dead end from our list of explored points (so it doesn't show up in our final path.)
        return False                                                #Tells the function that called it that we've reached a dead end.


#Testing
def main():
    print_maze(sample_maze())                                       #Print's the original maze for comparison.                                    
    dfs(sample_maze(),(5,0),[])

if (__name__ == "__main__"):
    main()