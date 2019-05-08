# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap





    return arr


# TO-DO:  implement the Bubble Sort function below

# Solution with recursion

# def bubble_sort( arr ):
#     swapped = False
#     for i in range(0, len(arr) - 1):       
#         if arr[i] > arr[i+1]:
#             swapped = True
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp
#     if swapped == True:
#         return bubble_sort(arr)
#     else:
#         return arr

# Iterative solution using a while loop

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#         for i in range(0, len(arr) - 1):

#     return arr