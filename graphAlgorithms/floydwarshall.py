#shortest path between all pairs of vertices, negatives edges allowed

import math

def floyd_warshall(graph):
  """
  Finds the shortest paths between all pairs of vertices in a weighted graph.

  Args:
      graph: A n x n matrix representing the adjacency matrix of the graph.
              Elements with infinity (e.g., math.inf) represent no edge.

  Returns:
      A n x n matrix representing the shortest distances between all pairs of vertices.
  """
  n = len(graph)

  # Initialize distance matrix with original weights
  distances = [[math.inf if x == math.inf else x for x in row] for row in graph]
  
  # Floyd-Warshall algorithm
  for k in range(n):
    for i in range(n):
      for j in range(n):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

  # Check for negative-weight cycles
  for i in range(n):
    if distances[i][i] < 0:
      raise ValueError("Graph contains a negative-weight cycle")

  return distances

# Example usage
graph = [
    [0, 3, math.inf, 7],
    [math.inf, 0, 4, 1],
    [1, math.inf, 0, 5],
    [6, 2, math.inf, 0]
]

distances = floyd_warshall(graph)

# Print the shortest distance matrix
for row in distances:
  print(row)