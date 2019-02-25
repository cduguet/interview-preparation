# Sorting

- In place 
- In other place, more memory but  faster

## Bubble sort
Naive Approach. Its name because every element moves up like a bubble.
- Complexity: O(n^2)
- Space Complexity: O(1)

## Merge Sort: 
- Divide and Conquer
     |8|3|1|7|0|10|2|
|8| |3| |1| |7| |0| |10| |2|
   |8| |1|3| |0|7| |2|10|
     |1|3|8| |0|2|7|10|
      |0|1|2|3|7|8|10|
- Complexity: O(nlog(n))
- Space Complexity: O(n)

## Quicksort:
- choose an arbitraty pivot
- put all elements less than pivot to the left, greater than to the right. 
- recurse on the left sub-array and right sub-array
- Complexity: O(n2) worse, or O(nlog(n)) average
- Space Complexity: O(1)

