#!/usr/bin/env python3

"""
Python code associated with graph-coloring based
solution to a sudoku puzzle.
"""

import networkx
import matplotlib.pyplot as plt

SIZE = 4

def blank_graph_edges(graph, dim):
    """
    Returns edges for a blank graph based on the dimension.
    """
    for x in range(1, 16, 4):
        for i in range(x, x+3):
            for j in range(i+1,x+4):
                graph.add_edge(i,j)

    for x in range(1,5):
        for i in range(x,x+9,4):
            for j in range(i+4,x+13,4):
                graph.add_edge(i,j)

    graph.add_edges_from([(1,6), (2, 5), (3, 8), (4, 7), (9, 14), (10, 13), (11, 16), (12, 15)])
    return graph


def create_blank_graph(dim):
    """
    Returns blank sudoku graph of specified dimensions.
    Dimensions are for the ENTIRE row/column, not a
    single box (single box dimensios is sqrt(dim).
    """
    graph = networkx.Graph()
    graph.add_nodes_from(range(1, dim**2 + 1))
    blank_graph_edges(graph,dim)
    return graph


def optimal_spot(graph, adj):
    pos = 0
    max = 0
    for k in adj.keys():
        if graph.nodes[k]['color'] == "":
            count =0
            for p in adj[k].keys():
                if graph.nodes[p]['color'] != "":
                    count+=1
            if count>max:
                max= count
                pos = k
    return pos


def choose_color(graph, adj):
	position = optimal_spot(graph, adj)
	adjacentVertices = adj[position]
	usedColors = set()
	for vertex in adjacentVertices.keys():
		usedColors.add(graph.nodes[vertex]['color'])
	for color in range(1, SIZE+1):
		if color not in usedColors:
			return color


def main():
    input_string=['3', '', '4', '2', '', '', '', '', '', '', '', '', '2', '', '', '3']
    sudoku = create_blank_graph(4)
    for l in range(len(input_string)):
        sudoku.nodes[l+1]["color"]=input_string[l]
    adjacent = networkx.to_dict_of_dicts(sudoku)
    pos = optimal_spot(sudoku,adjacent)
    print(pos)
    print('COLOR TO CHOOSE: ' + str(choose_color(sudoku, adjacent)))
    plt.subplot(121)
    networkx.draw(sudoku, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == '__main__':
    main()
