#shortest path from one node to all nodes, negative edges allowed
def bellman_ford(graph, source):
  """
  Finds the shortest paths from a source node to all other nodes in a weighted graph,
  handling graphs with negative weight edges.

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are dictionaries
              with neighboring nodes as keys and edge weights as values.
      source: The starting node (key) from which to find shortest paths.

  Returns:
      A dictionary containing distances from the source to all reachable nodes, 
      or None if a negative-weight cycle is detected.
  """
  n = len(graph)
  distances = {node: float('inf') for node in graph}
  distances[source] = 0

  # Relaxation process (repeated n-1 times)
  for _ in range(n - 1):
    for node, neighbors in graph.items():
      for neighbor, weight in neighbors.items():
        distances[neighbor] = min(distances[neighbor], distances[node] + weight)

  # Check for negative-weight cycles (one more relaxation)
  for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
      if distances[neighbor] > distances[node] + weight:
        return None  # Negative-weight cycle detected

  return distances

# Example usage
graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'D': 2, 'E': 3},
  'C': {'D': 3, 'E': 1},
  'D': {'C': -5},  # Negative weight edge
  'E': {}
}

source = 'A'

distances = bellman_ford(graph, source)

if distances is None:
  print("Graph contains a negative-weight cycle")
else:
  print("Distances from", source)
  for node, distance in distances.items():
    if distance != float('inf'):
      print(node, ":", distance)