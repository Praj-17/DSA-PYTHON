# Define a function to implement the Floyd-Warshall algorithm
def floyd_warshall(graph):
  # Initialize the distances between each pair of vertices as the weight of the edge between them, or as infinity if no such edge exists
  distances = [[float('inf') if i != j else 0 for i in range(len(graph))] for j in range(len(graph))]
  for u, v, weight in graph:
    distances[u][v] = weight

  # Iterate over each pair of vertices, updating the distances between them if a shorter path is found
  for k in range(len(graph)):
    for i in range(len(graph)):
      for j in range(len(graph)):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

  return distances

# Define an example graph
graph = [
  (0, 1, 3),
  (1, 2, 1),
  (2, 0, 7),
  (1, 3, 2),
  (3, 2, 1)
]

# Find the shortest paths in the graph using the Floyd-Warshall algorithm
distances = floyd_warshall(graph)

# Print the distances between each pair of vertices
for i in range(len(graph)):
  for j in range(len(graph)):
    print(f"The shortest distance from {i} to {j} is {distances[i][j]}")
