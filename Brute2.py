from itertools import permutations
import time
def tsp(distances):
    # Number of nodes
    numNodes = len(distances)
    nodes = list(range(1, numNodes))

    minCost = float('inf')
    optimal_path = []
    

    # Generate all permutations of the remaining nodes
    for perm in permutations(nodes):
        
        currCost = 0
        currNode = 0
        path = [0]  

        # Calculate the distances of the current permutation
        for node in perm:
            currCost += distances[currNode][node]
            currNode = node
            path.append(currNode)

        # Add the distances to return to the starting node
        currCost += distances[currNode][0]
        path.append(0)  # Return to the starting node

        # Update the minimum distances if the current distances is lower
        if currCost < minCost:
            minCost = currCost
            optimal_path = path
    
    return minCost, optimal_path



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

start_time = time.time()
min_cost, path = tsp(distances)
end_time = time.time()
execution_time = end_time - start_time
print(f"Minimum distances: {min_cost}")
print(f"Optimal path: {path}")
print(f"Calculation time: {execution_time:.6f} seconds")





