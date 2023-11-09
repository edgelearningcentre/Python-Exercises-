# Pythagorean Triplet

"""
Given an array arr of n integers,
write a function that returns true if there is a triplet (a, b, c) from the array
(where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

Example 1:

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.
Example 2:

Input:
N = 3
Arr[] = {3, 8, 5}
Output: No
Explanation: No such triplet possible.
Your Task:
You don't have to take any input or print any thing.
You have to complete the function checkTriplet() which takes an array arr,
a single integer n, as input parameters and returns boolean denoting answer to the problem.
"""

N = 5
Arr = [3, 2, 4, 6, 5]

def triplet_before_k(arr, k ):
    target = arr[ k ]
    
    if k < 2:
        return False
        
    if arr[0] + arr[1] > target or arr[k - 2] + arr[k - 1] < target:
        return False
        
    left = 0
    right = k - 1        
    while left < right:
        if arr[ left ] + arr[ right ] > target:
            right -= 1
        elif arr[ left ] + arr[ right ] < target:
            left += 1
        else:
            return True
            
    return False
        
def checkTriplet(arr, n):

    arr = list( set( arr ) )
    n = len( arr )
    for i in range( n ):
        arr[i] = arr[i] * arr[i]
    # print( f'arr is now {arr}' )
    arr.sort()

    for last in range( n - 1, -1, -1 ):
        if triplet_before_k( arr, last ):
            return True

    return False

out = checkTriplet(Arr,N)
print(out)
