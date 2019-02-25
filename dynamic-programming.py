
#calculate the number of subsets which make the sum 

# [2,4,6,10] ->

# - positive integers only?
# - only sum?
# - sorted?
# - are there duplicates? 
# - what do return for 0? 

def count_sets(arr, total):
    #return amount of subsets complying

    #start from right to left in array
    return rec(arr, total, len(arr)-1)

def rec(arr, total, i):
    if total == 0:
        return 1
    else if total < 0:
        return 0
    if i < 0:
        return 0
    if total < arr[i]: #if element already bigger than total, ignore
        return rec(arr, total, i-1)
    else:
        return rec(arr, total-arr[i], i-1) + rec(arr, total, i-1) 


## Memoization:

def count_sets_memo(arr, total):
    return dp(arr, total, arr.length-1, )