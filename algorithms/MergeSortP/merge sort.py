def merge_sort(list_int):
    '''(List of Int) -> (Sorted List of int)
    Given a List of integers this function returns another List contains the
    same integers but sorted in ascending order.
    '''
    result = [];
    if(list_int == []):
        # if the list is empty then return an empty list
        result = list_int
    elif(len(list_int) == 1):
        result = list_int
    else:
        # if list is not empty then divide recurse and then merge using
        # the two finger algorithm
        # dividing the list into two
        m = len(list_int) // 2
        # recurse
        left = merge_sort(list_int[0:m])
        right = merge_sort(list_int[m:])
        while(len(left) > 0 and len(right) > 0):
            if(left[0] > right[0]):
                result.append(right[0])
                right = right[1:]
            elif(left[0] < right[0]):
                result.append(left[0])
                left = left[1:]
            else:
                result.append(left[0])
                left = left[1:]
        # if left becomes empty and right is not then attach right to end
        # else attach right to the end of the result
        if(len(left) > 0):
            result = result + left
        elif(len(right) > 0):
            result = result + right
    return result