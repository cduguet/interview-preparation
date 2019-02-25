"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    # less = []
    # equal = []
    # greater = []

    # if len(array) > 1:
    #     pivot = array[0]
    #     for x in array:
    #         if x < pivot:
    #             less.append(x)
    #         if x == pivot:
    #             equal.append(x)
    #         if x > pivot:
    #             greater.append(x)
    #     # Don't forget to return something!
    #     return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # # Note that you want equal ^^^^^ not pivot
    # else:
        # return array

    # new approach:
    quicksort2(array, 0, len(array)-1)
    return array
    
def quicksort2(array, left, right):
    if left >= right:
        return
    pivot = array[right]
    print "array {}".format(array)
    print "quicksort. left: {}, right: {}, pivot: {}".format(left, right, pivot)
    index = partition(array, left, right, pivot)    
    quicksort2(array, left, index-1)
    quicksort2(array, index, right)
    
def partition(array, left, right, pivot):
    while left < right:
        while array[left] < pivot:
            left+=1
        while array[right] > pivot:
            right-=1
        print "left : {}".format(left)
        print "right: {}".format(right) 
        if left < right:
            swapp(array, left, right)
            left+=1
            right-=1
    return left
        
def swapp(array, left, right):
    swapp_el = array[left]
    array[left] = array[right]
    array[right] = swapp_el

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    # [6, 4, 1, 3, 9, 20, 25, 21, 21, 14]
print quicksort(test)