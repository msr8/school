def linear_search(lis:list, val, default:int=-1):
    for i,elem in enumerate(lis):
        if elem == val: return i
    else:
        return default



lis = [5,3,7,8,1]
print(linear_search(lis, 19))






'''
Linear search, also known as sequential search, is a simple algorithm for finding a target value within \
an array or a list. The algorithm sequentially checks each element of the list until a match is found or \
the end of the list is reached

Here's how the linear search algorithm works:
1) The algorithm takes an input array arr and a target value target as parameters
2) It starts at the first element of the array (arr[0]) and compares it to the target value. If the two values match, the algorithm returns the index of the first occurrence of the target value in the array
3) If the first element does not match the target value, the algorithm moves on to the second element (arr[1]) and compares it to the target value. If the two values match, the algorithm returns the index of the second occurrence of the target value in the array
4) The algorithm continues this process for each element of the array until either a match is found or the end of the array is reached
5) If the target value is not found in the array, the algorithm returns a special value (usually -1) to indicate that the value was not found

Linear search has a time complexity of O(n), where n is the length of the input array. This means that the \
time taken by the algorithm increases linearly with the size of the input
'''