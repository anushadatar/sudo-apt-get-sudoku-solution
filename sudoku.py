#!/usr/bin/env python3

"""
Python code associated with graph-coloring based solution to a sudoku puzzle.

To solve a puzzle, provide a string with all of the pre-filled in numbers 
(or empty strings for blank boxes) as the value of input_string in the main 
method. The program will compute the solution using graph coloring and print
it to the console.
"""

import math
import networkx as nx

def create_general_graph(size):
    """
    Create a blank sudoku graph with the specified size (as row length).

    size : Integer value of the row length of the graph.
    
    returns : Networkx graph of stated size with sudoku edges.
    """
    # Populate rows and columns.
    rowLists = []
    for row in range(size):
        listOfNums = [*range(row*size+1, row*size + size+1, 1)]
        rowLists.append(listOfNums)
    columnLists = []
    for column in range(size):
        listOfNums = [*range(column+1, size*size+1, size)]
        columnLists.append(listOfNums)
    # Connect edges for each of the inner grids of the graph.
    boxLists = []
    boxStarts = get_box_nums(size)
    for start in boxStarts:
        boxList = []
        for row in range(int(math.sqrt(size))):
            for i in range(int(math.sqrt(size))):
                boxList.append(start + row*size + i)
        boxLists.append(boxList)
    allLists = [rowLists, columnLists, boxLists]
    
    # Instantiate graph and connect edges based on lists.
    graph = nx.Graph()
    for nodeLists in allLists:
        for group in nodeLists:
            connectedGraph = nx.complete_graph((iter(group)), nx.Graph)
            graph = nx.algorithms.operators.binary.compose(graph, connectedGraph)
    return graph


def get_box_nums(size):
    """
    Get the coordinates for the positions on the graph of where the individual
    boxes of connected nodes must start.
    
    size : The integer length of a single row or column in the graph.
    
    returns : List of the indices for the start indices of the boxes (as ints).
    """

    boxStarts = []
    for row in range(0, size, int(math.sqrt(size))):
        for start in range(row*size+1, row*size + size+1, int(math.sqrt(size))):
            boxStarts.append(start)
    return boxStarts


def optimal_spot(graph, adj):
    """
    Determine the optimal spot to determine the color for, based on the number 
    of existing prepopulated vertices.
    
    graph : The networkx sudoku graph used in the problem.
    adj : The networkx dictionary adjacency matrix associated with the graph.
   
    returns : Integer index of the best vertex to find the color of.
    """
    pos = 0
    max = 0
    # Check the adjacency matrix to find the vertex with the highest number of
    # adjacent vertices that are colored.
    for k in adj.keys():
        if graph.nodes[k]['color'] == "":
            count = 0
            for p in adj[k].keys():
                if graph.nodes[p]['color'] != "":
                    count += 1
            if count > max:
                max = count
                pos = k
    return pos


def choose_color(graph, adj, position):
    """
    Determine which of the available colors should be placed in a given 
    position on the graph.

    graph : The networkx sudoku graph used in the problem.
    adj : The networkx dictionary adjacency matrix associated with the graph.
    position: The integerposition of the box to choose the color for.

    returns : Integer value of the color that the box should be.
    """
    adjacentVertices = adj[position]
    usedColors = set()
    unusedColors = []
    for vertex in adjacentVertices.keys():
        usedColors.add(graph.nodes[vertex]['color'])
    for color in range(1, int(math.sqrt(len(graph.nodes)))+1):
        if str(color) not in usedColors:
            unusedColors.append(color)
    return unusedColors


def fill_colors(graph):
    """
    Use a graph coloring strategy to populate the graph with the appropiate 
    colors to solve the puzzle. This method is recursively called by 
    populate_color when there are multiple possible paths to explore.

    graph : The graph networkx sudoku graph containing the puzzle to solve.
    returns : Networkx sudoku graph populated with values that solve the puzzle.
    """
    size = len(graph.nodes)
    adjacent = nx.to_dict_of_dicts(graph)
    pos = optimal_spot(graph, adjacent)
    # If there are no more positions left to fill, the graph is full.
    if pos == 0:
        return graph
    colors = choose_color(graph, adjacent, pos)
    # If there are possible colors left, try each path to look for a solution.
    if len(colors) != 0:
        for color in colors: 
            # Make a copy of the graph, add the color, run fill_colors again.      
            filled_graph = populate_color(graph.copy(), pos, color)    
            if is_populated(filled_graph):
                return filled_graph
            else:
                continue 

def populate_color(graph, pos, color):    
    """
    Place the next guess of the color for the chosen position in the graph and then iterate. 
   
    graph : The networkx sudoku graph for which to place the next color.
    pos   : The integer position at which to place the color.
    color : The string color to fill at the particular position. 

    returns : Graph with the populated color or the same graph if there are no colors left.
    """ 
    graph.nodes[pos]['color'] = str(color)
    new_graph = fill_colors(graph)           
    if (new_graph == None):
        return graph
    else:
        return new_graph

def is_populated(graph):
    """
    Returns whether or not that graph is completely populated (i.e. if 
    each box has been filled in.

    graph : The networkx sudoku graph to test.

    returns : True if each spot is filled in, False otherwise.
    """
    size = int(math.sqrt(len(graph.nodes)))
    colors = []                       
    for node in range(1, size*size+1):      
       colors.append(graph.nodes[node]['color'])
    for color in colors:
        if color == '':
            return False
    return True

def display_sudoku(graph):
    """
    Print the sudoku graph to the console.
    Prints blank spaces as "-" as to align numbers when visualizing.
   
    graph : Networkx sudoku graph to print to the console.
    """
    size = int(math.sqrt(len(graph.nodes)))
    colors = []
    for node in range(1, size*size+1):
        colors.append(graph.nodes[node]['color'])
    for i in range(size*size):
        if colors[i] == '': 
            colors[i] = '-'     
    for i in range(size):
        print(colors[i*size:i*size+size])
    print()


def main():
    # String containing the values to pre-populate in the sudoku board.
    # Additional test cases are stored in puzzle.txt.
    input_string = ['','','6','','','','7','','1','','','','','9','','','','','1','','4','8','','','','','5','9','5','','','','','4','','','','','7','','1','','9','','','','','1','','','','','7','6','2','','','','','5','6','','8','','','','','6','','','','','4','','9','','','','2','','']

    # Create and populate networkx graph for sudoku board.
    sudoku = create_general_graph(int(math.sqrt(len(input_string))))
    for l in range(len(input_string)):
        sudoku.nodes[l+1]["color"] = input_string[l]
    
    # Print the starting configuraton.
    print('Starting board:')
    display_sudoku(sudoku)
    # Run the algorithm and print the completed board.
    completed_board = fill_colors(sudoku)
    print('Completed board')
    display_sudoku(completed_board)

if __name__ == '__main__':
    main()
