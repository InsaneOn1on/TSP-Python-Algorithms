import time  

def tsp_held_karp(distances):
    n = len(distances)  # Number of cities
    memo = {}  # Memoization for Subsets Cost
    citymemo = {}  # Memoization for Subsets path

    # Dynamic programing function conatining (i, j)
    def dp(visited, pos):
        
        # If all cities are visited, return the cost to go back to the starting city
        if visited == (2 ** n) - 1:
            return distances[pos][0]

        # If we've already calculated the cost skip this
        if (visited, pos) in memo:
            return memo[(visited, pos)]

        ans = float('inf')  # Start with a high number for comparison
        best_next_city = -1  # Placeholder for the next city to visit

        # Check all possible next cities in the range of the graph
        for nxt in range(n):
            # If the city hasn't been visited yet
            if not visited & (2 ** nxt):
                # Calculate the total cost of visiting this city and others after it
                cost = distances[pos][nxt] + dp(visited | (2 ** nxt), nxt)
                if cost < ans:  # Update shortest cost
                    ans = cost
                    best_next_city = nxt

        # Memoize the results
        memo[(visited, pos)] = ans
        citymemo[(visited, pos)] = best_next_city
        return ans

    # Get the min distance back to the start 
    min_distance = dp(1, 0)

    # Reconstruct the path 
    path = []  # Stores the optimal path
    visited = 1  # Start with only city 0 visited
    current_pos = 0  # Start at city 0

    while True:
        path.append(current_pos)  # Add the current city to the path
        next_city = citymemo.get((visited, current_pos))  # Find the next city to visit
        if next_city is None:  # If there’s no next city, we’re done
            path.append(0)  # Add the starting city to complete the loop
            break
        visited |= (2 ** next_city)  # Mark the next city as visited
        current_pos = next_city  # Move to the next city

    # Return the shortest distance and the optimal path
    return min_distance, path

distances = distances = [
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






# Measure the execution time
start_time = time.time()
min_distance, path = tsp_held_karp(distances)
end_time = time.time()

# Print the results
execution_time = end_time - start_time
print("Minimum distance:", min_distance)
print("Optimal path:", path)
print(f"Calculation time: {execution_time:.6f} seconds")








