# shortest_path_finder from source to destination
# Using Breadth-First-Search(BFS) algorithm 
# @Pratheeka_m_u
# (C) - 2022 Pratheeka_m_u, Karnataka, India 
# email - pratheekmundigesara389@gmail.com

import curses
from curses import wrapper
import queue
import time
# '--pip install windows-curses--' to use curses module 

# Feel free to change the maze
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*4, "X", RED)
            else:
                stdscr.addstr(i*2, j*4, value, BLUE)


# To find the position of the starting vertex
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    # set() to keep track of the visited nodes
    visited = set()
    visited.add(start_pos)

    # until every element in the queue popped out 
    # i.e until the queue becomes empty
    while not q.empty(): 
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.3)
        stdscr.refresh()

        if maze[row][col] == end:
            #print(path)
            return path

        neighbours = find_neighbours(maze, row, col)

        for neighbour in neighbours:
            if neighbour in visited:
                continue
            
            r, c = neighbour # r->row c->column of neighbour
            if maze[r][c] == '#': # "#" means obstacle in this context
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))

            visited.add(neighbour)


def find_neighbours(maze, row, col):
    neighbours = []

    if row > 0: # Above neighbour
        neighbours.append((row - 1, col))
    if row + 1 < len(maze): # Below neighbour
        neighbours.append((row + 1, col))
    if col > 0: # Left neighbour
        neighbours.append((row, col - 1))
    if col + 1 < len(maze[0]): # Right neighbour
        neighbours.append((row, col + 1))

    return neighbours #return final neighbours list


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
