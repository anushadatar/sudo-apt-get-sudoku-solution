#!/usr/bin/env python3

"""
Python code associated with graph-coloring based
solution to a sudoku puzzle.
"""

import networkx
import matplotlib.pyplot as plt

def blank_graph_edges(graph, dim):
    """
    Returns edges for a blank graph based on the dimension.
    """
    for x in range(1,13,4):
        for i in range (x,x+2):
            for j in range(i+1,i+3):
                graph.add_edge(i,j)

    for x in range (1,4):
        for i in range(x,x+8,4):
            for j in range(i+4,i+12,4)
                graph.add_edge(i,j)

    add_edges_from([(1,6), (2, 5), (3, 😎, (4, 7), (9, 14), (10, 13), (11, 16), (12, 15)])
    add_edges_from([(1,6), (2, 5), (3, 8 ), (4, 7), (9, 14), (10, 13), (11, 16), (12, 15)])
    return graph

def create_blank_graph(dim):
    """
    Returns blank sudoku graph of specified dimensions.
    Dimensions are for the ENTIRE row/column, not a
    single box (single box dimensios is sqrt(dim).
    """
    graph = networkx.Graph()
    graph.add_nodes_from(range(1, dim**2 + 1))
    graph.add_edges_from(blank_graph_edges(dim))
    return graph

def main():
    create_blank_graph(4)

if __name__ == '__main__':
    main()
    print("Ran main method")
