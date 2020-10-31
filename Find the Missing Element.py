'''Problem
    Consider an array of non-negative integers.A second array is formed by shuffing the elements
    of first array and deleting a random element. Given these two arrays,Find which element is missing
    in second array.
    for eg.
    Input: finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    Output: 5 is the missing number
    '''

'''Approach
    1. By brut force go through every element in second array and check in first array. 
    complexity  O(N^2)
    2. Sort first array then binary search . complexity O(NlogN)
    Note : special notice for duplicate items
    3. If we don't deal with special case then sort both array and once two iterator have
    different value the value of first iterator is missing element. 
    complexity O(NlogN)'''

#Solution 1

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()


    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

# zip([1,2,3],[4,5,6])
#[(1, 4), (2, 5), (3, 6)]

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
result = finder(arr1,arr2)
print(result)



#Solution 2

import collections

def finder2(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1     #In normal dict it is not allowed and through an error but in default it possible

    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1

result2 = finder2(arr1,arr2)
print(result2)

#Solution 3 (Cleaver Trick for linear algo) but not useful if input in decimal places or
# too large input or too large value

def finder3(arr1,arr2):
    result3 =0

    #Perform an XOR between the numbers in the arryas
    for num in arr1+arr2:
        result3^=num
        print(result3)
    return result3

finder3(arr1,arr2)

#Solution 4 By adding all element in 1 & 2 and then subtract and the missing value is finded