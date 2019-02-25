# Shortest Path Problem

- Unweighted Graph. Find the path with the least number of edges. -> BFS


# Dijkstra's Algorithm

Shortest path for weighted graphs. 

- Create a list of distances to all nodes. Initialize them to infinity, and the start node to 0. 

 - Store all the nodes in a queue ordered by distance (**Min Priority Queue**). Choose to explorer further on the  node with the minimum value (**Greedy approach**). 

 - Remove Minimum node (Extract Min) and explore on the connections of that node, then update the nodes with the new distance values (replace if they are lower). 

 - Repeat with minimum element of the queue again. 

 - Will end when found the goal or when the rest of nodes have a distance of infinity. In this case, the search was failure.

 - Worst Case: `O(|V|^2)`


 # Knapsack Problem

I have a backpack and want to put elements with weight and value. 

*How can I maximize value for a given weight?* 

0-1 Knapsack. We have only one version of each object. 

- Bruteforce: `O(2^n)`

- Make Table of all max values for small weights. `O(nW)`, `n=no. elements`, `W=max weight`


# Dynamic Programming 

Breaking a bigger problem in subproblems (smaller problem). 

- Base case: Smallest computation.

- Lookup table: store solutions to subproblems

- Memoization: Storing precomputed Values

- Equation to find combinations to expand based on lookup table values

# Traveling Salesman Problem (TSP)

_Giving a group of cities, and distance between them, find the shortest path to visit every city and come back to the starting point._

**NP-Hard**: Problem who don't have a known Exact Polynomial-time solution. 

Two Solutions Types: 
- Exact Algorithms (but in non-poly-time):
    - **Brute Force**: `O(n!)`
    - **Held-Karp Algorithm (Dynamic Programming)**: `O(n^2*2^n)`

- Approximation (but poly-time):
    - **Christophides Algorithm**: Solution is at most 50% longer than shortest route. 
