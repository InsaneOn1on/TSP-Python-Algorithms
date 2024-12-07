import time

def nearest_neighbor(distances):
    
    numNodes = len(distances)
    visited = [False] * numNodes  # Keeps track of visited nodes
    path = [0]  # Start at node 0 
    visited[path[0]] = True  # Mark the start node as visited
    min_distance = 0
    current_node = 0  # Initialize as 0
    

    # Visit the remaining nodes
    for _ in range(numNodes - 1):
        nearest_node = None
        nearest_dist = float('inf')

        # Find the nearest unvisited node
        for next_node in range(numNodes):
            if not visited[next_node] and distances[current_node][next_node] < nearest_dist:
                nearest_node = next_node
                nearest_dist = distances[current_node][next_node]

        # Move to the nearest node
        visited[nearest_node] = True
        path.append(nearest_node)
        min_distance += nearest_dist
        current_node = nearest_node

    # Add the distances to return to the starting node
    min_distance += distances[current_node][0]
    path.append(0) # add final node to the path

    return min_distance, path


distances = [
    [0, 10, 15, 20, 30, 40, 50, 1, 3, 11, 25, 18],
    [10, 0, 25, 25, 2, 5, 0, 6, 21, 14, 22, 27],
    [15, 25, 0, 30, 6, 8, 10, 70, 17, 90, 35, 40],
    [20, 30, 6, 0, 45, 32, 2, 10, 60, 13, 50, 48],
    [30, 40, 5, 3, 0, 18, 16, 24, 29, 40, 15, 22],
    [40, 50, 0, 18, 10, 0, 18, 9, 11, 30, 28, 35],
    [50, 1, 6, 70, 15, 60, 0, 30, 50, 40, 10, 45],
    [1, 6, 21, 17, 60, 60, 35, 0, 7, 18, 14, 16],
    [3, 21, 14, 90, 13, 18, 16, 40, 0, 35, 12, 18],
    [11, 14, 17, 4, 14, 30, 24, 12, 19, 0, 8, 30],
    [25, 22, 35, 50, 15, 28, 10, 14, 12, 8, 0, 20],
    [18, 27, 40, 48, 22, 35, 45, 16, 18, 30, 20, 0]
]

# Measure execution time
start_time = time.time()
min_distance, path = nearest_neighbor(distances)
end_time = time.time()

execution_time = end_time - start_time
print("Path:", path)
print("Total cost:", min_distance)
print(f"Execution time: {execution_time:.6f} seconds")


