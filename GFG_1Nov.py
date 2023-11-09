# !Python3
# Frequencies of Limited Range Array Elements
"""
Given an array arr[] of N positive integers which can contain integers from 1 to P
where elements can be repeated or can be absent from the array.
Your task is to count the frequency of all numbers from 1 to N. Make in-place changes in arr[],
such that arr[i] = frequency(i). Assume 1-based indexing.
Note: The elements greater than N in the array can be ignored for counting
and do modify the array in-place. 



Example 1:
Input:
N = 5
arr[] = {2, 3, 2, 3, 5} 
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
"""


def frequencyCount(arr, N, P):
        # code here
        count=[]
        for i in range(N):
            count.append(0)
        for i in range(N):
            if(N>=arr[i]):
                count[arr[i]-1]+=1
            else:
                continue
        for i in range(N):
            arr[i]=count[i]


N = 5
arr = [2, 3, 2, 3, 5]
P = 5

# def frequencyCount(arr, N, P):
 
#     dic={}     
#     for i in arr:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]=dic.get(i)+1
    
#     for i in range(1,N+1):
#         if i in dic.keys():
#             arr[i-1]=dic.get(i)
#         else:
#             arr[i-1]=0
#     return arr 

bb = frequencyCount(arr,N,P)
print(bb)
