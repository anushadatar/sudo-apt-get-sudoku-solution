#!/usr/bin/env python3

"""
Python code associated with graph-coloring based
solution to a sudoku puzzle.
"""

import networkx 

def blank_graph_edges(dim):
    """
    Returns edges for a blank graph based on the dimension.
    """
    pass

def create_blank_graph(dim):
    """
    Returns blank sudoku graph of specified dimensions.
    Dimensions are for the ENTIRE row/column, not a 
    single box (single box dimensios is sqrt(dim).
    """
    graph = networkx.Graph()
    graph.add_nodes_from(range(1, dim**2 + 1))
    graph.add_edges_from(blank_graph_edges(dim))
