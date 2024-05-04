#Dijktra's algorithm is really good for finding the shortest path from one node to all nodes
from heapq import heappush, heappop


def dijkstra(graph, source):
  """
  Finds the shortest paths from a source node to all other nodes in a weighted graph.

  Args:
      graph: A dictionary representing the graph. Keys are nodes, values are dictionaries
              with neighboring nodes as keys and edge weights as values.
      source: The starting node (key) from which to find shortest paths.

  Returns:
      A dictionary containing distances from the source to all other nodes
      and another dictionary containing the previous node in the shortest path.
  """
  n = len(graph)
  distances = {node: float('inf') for node in graph}
  distances[source] = 0
  pq = [(0, source)]  # priority queue with (distance, node)

  while pq:
    current_dist, current_node = heappop(pq)

    if current_dist > distances[current_node]:
      continue  # already processed with a shorter distance

    for neighbor, weight in graph[current_node].items():
      new_dist = current_dist + weight
      if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        heappush(pq, (new_dist, neighbor))

  # predecessor for path reconstruction (optional)
  predecessors = {node: None for node in graph}
  for node, distance in distances.items():
    if distance != float('inf'):
      for neighbor, weight in graph[node].items():
        if distances[neighbor] == distance + weight:
          predecessors[neighbor] = node

  return distances, predecessors

# Example usage
graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'D': 2, 'E': 3},
  'C': {'D': 3, 'E': 1},
  'D': {},
  'E': {}
}

source = 'A'

distances, predecessors = dijkstra(graph, source)

print("Distances from", source)
for node, distance in distances.items():
  print(node, ":", distance)

# Reconstruct shortest path if needed (using predecessors)