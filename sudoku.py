#!/usr/bin/env python3

"""
Python code associated with graph-coloring based
solution to a sudoku puzzle.
"""

import networkx as nx
import math
import matplotlib.pyplot as plt

# The length of each row/column on the sudoku board.
SIZE = 4

def create_general_graph(size):
    """
    Create a general sudoku graph for specified size.

    size : Integer value of the row length of the graph.
    returns : networkx sudoku graph of stated size.
    """
    rowLists = []
    for row in range(size):
        listOfNums = [*range(row*size+1, row*size + size+1, 1)]
        rowLists.append(listOfNums)
    columnLists = []
    for column in range(size):
        listOfNums = [*range(column+1, size*size+1, size)]
        columnLists.append(listOfNums)
    # print(rowLists)
    # print(columnLists)
    boxLists = []
    boxStarts = get_box_nums(size)
    # print('boxstarts: ' + str(boxStarts))
    for start in boxStarts:
        boxList = []
        for row in range(int(math.sqrt(size))):
            for i in range(int(math.sqrt(size))):
                boxList.append(start + row*size + i)
        boxLists.append(boxList)
    # print(boxLists)
    allLists = [rowLists, columnLists, boxLists]
    # print(allLists)
    graph = nx.Graph()
    for nodeLists in allLists:
        for group in nodeLists:
            connectedGraph = nx.complete_graph((iter(group)), nx.Graph)
            graph = nx.algorithms.operators.binary.compose(graph, connectedGraph)
    # print(list(graph.nodes()))
    return graph


def get_box_nums(size):
    """
    Get the coordinates for the positions on the graph.
    
    size : The length of a single row or column in the graph.
    returns : List of the indices for the graph.
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
    
    graph : The sudoku graph used in the problem.
    adj : The adjacency matrix associated with the graph.
    """
 
    pos = 0
    max = 0
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
    Determine which of the available colors should be placed
    in a given position.

    graph : The sudoku graph used in the problem.
    adj : The adjacency matrix associated with the graph.
    position: The position of the box to choose the color for.

    color: Returns integer value of the color that the box should be.
    """
    # position = optimal_spot(graph, adj)
    adjacentVertices = adj[position]
    usedColors = set()
    for vertex in adjacentVertices.keys():
        usedColors.add(graph.nodes[vertex]['color'])
    for color in range(1, SIZE+1):
        if str(color) not in usedColors:
            return color


def fill_colors(graph):
    """
    Use a graph coloring strategy to populate the graph
    with the appropiate colors to solve the puzzle.

    graph : The graph containing the puzzle to solve.
    """
    colored = 0
    size = len(graph.nodes)
    for node in graph.nodes:
        if graph.nodes[node]['color'] != '':
            colored += 1
    while (colored < size):
        # display_sudoku(graph)
        adjacent = nx.to_dict_of_dicts(graph)
        pos = optimal_spot(graph, adjacent)
        color = choose_color(graph, adjacent, pos)
        graph.nodes[pos]['color'] = str(color)
        colored += 1


def display_sudoku(graph):
    """
    Print the sudoku graph to the console.
    
    graph : Graph to print to the console.
    """
    size = int(math.sqrt(len(graph.nodes)))
    colors = []
    for node in range(1, size*size+1):
        colors.append(graph.nodes[node]['color'])
    for i in range(size):
        print(colors[i*size:i*size+size])
    print()


def main():
    # String containing the values to pre-populate in the sudoku board.
    input_string = ['3', '', '4', '2', '', '', '', '', '', '', '', '', '2', '', '', '3']

    # Create and populate networkx graph for sudoku board.
    sudoku = create_general_graph(SIZE)
    for l in range(len(input_string)):
        sudoku.nodes[l+1]["color"] = input_string[l]
    # print(adjacent)
    print('Starting board:')
    display_sudoku(sudoku)
    fill_colors(sudoku)
    print('Completed board')
    display_sudoku(sudoku)
    # plt.subplot(121)
    # nx.draw(sudoku, with_labels=True, font_weight='bold')
    # plt.show()

if __name__ == '__main__':
    main()
