# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math

def merge( arrA, arrB ):
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    ## This allocates space for the array properly, without relying on
    ## python to defaultly assign space for the data
    a = 0
    b = 0
    for i in range(0, num_elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        midpoint = len(arr)//2
        left = merge_sort(arr[0:midpoint]) 
        right = merge_sort(arr[midpoint:])
        print(left, "arrayA")
        print(right, "arrayB")
        return merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
