# *sudo apt-get sudoku-solution*
A python sudoku solver as an investigation of graph coloring algorithms for Olin College Discrete Mathematics FA19 Homework 5 Investigation by Diego Berny, Jordan Crawford-O'Banner, and Anusha Datar.

# Graph Coloring
The **coloring** of a simple graph refers the configuration where each vertex of the graph is assigned a color such that no two adjacent vertices are given the same color. For most graphs, a coloring of interest has the lowest possible number of unique colors. This minimum quantity of colors is called the **chromatic number** of the graph. While graph coloring problems often consider the vertices of a simple graph, the same principles extend to problems such as coloring the regions of a planar graph such that no set of adjacent regions match.

The **four color theorem** asserts that for any planar graph (a graph where no edge crosses another edge), the chromatic number of that planar graph is no greater than four. While this theorem was proposed as a conjecture in the 1850s, it was not formally proven until 1976. Prior to that, there were both fallacious proofs that were accepted (and then later rejected) and adoption of approximations like the Five Color Theorem. The actual four color theorem was proven in 1979 using a computer program that eliminated each possible type of counterexample. This proof was one of the first major computer-aided proofs.

The study of graph coloring has a variety of practical applications - classic ones include scheduling and register allocation. We chose to explore the application of graph coloring to solving Sudoku puzzles. 

# The Sudoku Graph
Sudoku puzzles require players to populate boxes within a grid with numbers such that each row, column, and box contains a set of unique digits. Each puzzle contains preloaded clues to constrain the total number of possible solutions.  
These puzzles can be represented as sudoku graphs, which are undirected graphs where each node is connected to each additional node in its row, each additional node in its column, and each node in its box. Because some of the boxes are prepopulated, applying graph coloring to sudoku involves the **precoloring extension** special case of the general graph coloring problem.

<p align="center">
  <img src="https://i.gyazo.com/dc6b6fd8b23f778ca57a14906a9f5eea.png" width="300px" height="300px"/></p>
  <p align="center">Image of Sudoku Graph, from Wikipedia<p align="center">

# Graph Coloring for Sudoku
## Implementation

- general explanation of algorithm + connections to graph theory, depending on whether or not we backtrack
- probably some graphics/screenshots/code pictures

## Evaluation

- Talk about runtime depending on how far we get.

In general, graph coloring is computationally complex. Finding the chromatic number of a graph is an NP-hard problem. NP stands for non-deterministic polynomial acceptable problems, and problems that are NP-hard are at least as difficult as problems that are NP-Complete. NP-Complete problems cannot be solved in polynomial time, but a potential solution can be validated in polynomial time - so solving the problem requires exhaustively testing all types of possible cases, which is both time and computationally intensive. Meanwhile, finding a 3-coloring for a graph is an NP-complete problem. While advances in graph theory and computational infrastructure mean that solving these NP-hard/NP-complete problems is certainly possible, there is still great overhead associated with them,
