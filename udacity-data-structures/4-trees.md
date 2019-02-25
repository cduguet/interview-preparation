# Trees

```                
                            Level Height Depth
      rootNode                1     2      0
       /     \
   child1    child2           2     1      1
     |        /     \
leafNode leafNode leafNode    3     0      2
```


# Traverse
```
       D
      / \
     B   E
    / \   \
   A   C   F
```

## Depth-First Search (DFS)
Visit child nodes first.  
- Pre-Order: 
` => D,B,A,C,E,F`
- In-Order:
` => A,B,C,D,E,F`
- Post-Order:
` => A,C,B,F,E,D`
## Breadth-First Seach (BFS): Level Traversal
Visit nodes of same level first.
- Level Order Traversal:   
from top to bottom, left to right:
`=> D,B,E,A,C,F`
Pseudocode: 
```
  queue  = []  
  while queue: 
    a = queue.pop()
    a.process()
    q.append(a.children())
```

# Search and Delete:
- Search is `O(n)`.  
- Deletion of a leaf is `O(1)`.
- Deletion of an internal node requires to replace it with one of its descendants. 
  - Deletion of a node with 1 children is `O(1)`
  - Deletion of a node with 2 children can be `O(height)`

# Insert
 Try to insert in the first childrenless node or with only one children. Worst case is O(heightOfTree) = O(log(n))

# Binary Search Tree (BST)
These are ordered BT 
```
       5
      / \
     3   8
    /   / \
   1   7  10
```
- Inserting on a BST: `O(log(n))`

- Search on a BST: O(height) = `O(log(n))`

- Deleting in a BST: `O(log(n))`


# Heaps
Can be binary (2-children) or not.

- Max Heaps: Parent > Child
- Min Heaps: Children > Parent 
```
    Max Heap        Min Heap
       7                1
      / \              / \
     5   3            2   3
    / \              / \  
   2   1            5   7  
```

- Heaps are **Complete**. Levels except last one MUST be full   
- Search. Worst: `O(n)` Avg: O(n/2)
- Insert -> Heapify. Compare with parent and swap. `O(log(n))`
- Remove -> Insert rightmost leaf -> Heapify. `O(log(n))`
- Array implementation saves space. No pointers needed. 

# Self Balanced Trees
Trees that try to minimize its levels.

## Red-Black Tree

```md
#               9      <- black node
               / \ 
#             4   16
             /      \              
<           1       25   <- red node               >
```
### Rules
1. Every node is either <font color="red">red</font> or <font color="black">black</font>
2. All NIL leafs must be black.
3. Red Node must have black children. 
4. Root must be black
5. Path from root to nil must always have same black nodes. 

### Insertion
- Red-Black Tree + BST rules 
- Insert <font color="red">red</font> Nodes only! 
- Worst case: O(log(n))

| case | description | what to do |
| :---:|      ---    | ---        |
| case 1 | Inserting root node | node -> black |
| case 2 | Parent is black | do nothing  | 
| case 3 | Parent and uncle red | parent,uncle -> black.  grandparent -> red. Then treat gp like new inserted-node | 
| case 4 | Parent is red, uncle is black/nil | rotate, recolor & done  

Order or rotations are: 

| Current Order | Rotation | 
| :---: | :---: |  
| (node to parent, parent to gp)| (first,second) |
| LL | R |
| RL | LR |
| RR | L |
| LR | RL |



