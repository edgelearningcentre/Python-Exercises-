#Minimum distance between two numbers

"""
You are given an array a, of n elements.
Find the minimum index based distance between two distinct elements of the array, x and y.
Return -1, if either x or y does not exist in the array.

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.

Input:
N = 7
A[] = {86,39,90,67,84,66,62}
x = 42, y = 12
Output: -1
Explanation: x = 42 and y = 12. We return
-1 as x and y don't exist in the array.

"""

def minDist(arr, n, x, y):
    x_position, y_position, min_distance = -1, -1, float("inf")

    for position in range(n):
        if x == arr[position]:
            x_position = position
        elif y == arr[position]:
            y_position = position

        if x_position != -1 and y_position != -1:
            min_distance = min(min_distance, abs(x_position - y_position))

    # If min_distance is still set to float("inf"), no valid pair of x and y found.
    return -1 if min_distance == float("inf") else min_distance


N = 7
arr = [86,39,90,67,84,66,62]
x = 42
y = 12

out = minDist(arr,N,x,y)
print(out)