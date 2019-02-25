# Graphs 
- Trees are a type of graph
```
        6
 Tokyo ---- Thailand          
     4\    /3
       Bali    
      /10  
    SF      
```


| Graph Classification | description | types|
| --- | --- | --- |
| Directivity | edges have direction?| - Directed <br/> - undirected | 
| Connectivity | are all nodes connected? |- Connected <br/> - Disconnected |
| Cyclic | do they form a loop? | - Cyclic <br/> - Acyclic |

- *Directed Acyclic Graph DAG*: Good for algoriths 

- *Connectivity*: The minimum no. of elememnts needed to be removed to make the Graph disconencted. 

 ## Connectivity of directed Graphs 

 | type | description | 
 | --- | --- |
 | disconnected | some vertices are not connected tot he rest of the graph  | 
 | weakly connected | some paths go in only one direction, but not the other. there can be a path from b to a but not form a to b.|
 | connected | a normal connected undirected graph | 
 | strongly connected |  a directed connected graph where there is always a way from A to B | 


 ## Graph Representation: 
```
0 - 1
  / | 
 2- 3
```

 - **Vertex, Edge Objects**:   
 `[Vertex<name,id,[edges]>], [Edge<strength,id,[vertex]>]`
 - **Edge List** :  
 `[[0,1], [1,2], [1,3], [2,3]]`
 - **Adjacency List**:  
 `[[1], [0,2,3], [1,3], [1,2]]`   
 - **Adjacency Matrix**:  
      `[[0, 1, 0, 0],`  
&nbsp; `[1, 0, 1, 1],`  
&nbsp; `[0, 1, 0, 1],`  
&nbsp; `[0, 1, 1, 0]]`


## Traversal

### DFS Depth First Search: *Use a Stack*   
This is like using In-Order, Post-Order or Pre-Order in trees

Look for the neighbor elements first, and if already seen come back to the one you were before.  

- Check Node and add children (directed to) to the stack
    - go to children from top of stack
    - mark as visited
    - (remember parent)
        - repeat recursively

`O(|E|+|V|)`  

https://www.cs.usfca.edu/~galles/visualization/DFS.html

 ### BFS Breadth first search: *Use a queue*
- This is like using level search in trees

You start at one node and start adding all elements connected to it to a queue. When we run out of edges, start dequing the nodes. 

- Check Node and all all children (directed to) to a Queue
   - go to children from deque
   - mark as visited
   - (remember parent)
     - repeat recursively

`O(|E|+|V|)`
 
https://www.cs.usfca.edu/~galles/visualization/BFS.html

## Eulerian Path
Path that travers through every edge in a path once.  Not every graph has an eulerian path. It can be created by merging multiple eulerian cycles. 
 - *Eulerian Cycle* :
Traverse in a cycle passing on edges only once. 

- A node has can only have eulerian cycles if all nodes have an even degree (even no. or edges). 
- But an eulerian path can be have odd nodes as long as they are the start and end of path. 

- *Algorithm*: Finding Eucledian Path: Find all eucledian cycles and merge them. `O(|E|)` 

## Hamiltonian Path
Must go through every vertex once. Will start and end with the same vertex. 


