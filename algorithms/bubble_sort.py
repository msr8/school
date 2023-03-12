lis     = [5,3,7,8,1]
lis_len = len(lis)

to_stop = False

print(f'0.0: {lis}\n\n')


c = 1
j = 0
while not to_stop:
    to_stop = True
    j = 1
    for i in range(0, lis_len-1):
        if lis[i] < lis[i+1]:
            lis[i], lis[i+1] = lis[i+1], lis[i]    # Swaps the elements
            to_stop = False                        # Tells the program that we had to swap elems, meaning the list might not be in order yet
        print(f'{c}.{j}: {lis}')
        j += 1
    c += 1




'''
Bubble sort is a simple sorting algorithm that repeatedly compares adjacent elements in a list and swaps them \
if they are in the wrong order. It repeatedly passes through the list until no more swaps are needed, indicating \
that the list is sorted

The algorithm works as follows:
1) Compare the first two elements of the list. If the first element is greater than the second element, swap them
2) Move to the next pair of elements (i.e., the second and third elements) and compare them. If they are in the wrong order, swap them
3) Continue comparing adjacent pairs of elements and swapping them if they are in the wrong order, until the end of the list is reached
4) If any swaps were made in step 3, repeat steps 1-3 until no more swaps are needed

Bubble sort has a time complexity of O(n^2) in the worst case scenario, which makes it inefficient for large lists. \
However, it has the advantage of being easy to understand and implement
'''


