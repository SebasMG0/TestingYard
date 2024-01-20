"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

    Example 1:

    Input: arr = [1,15,7,9,2,5,10], k = 3
    Output: 84
    Explanation: arr becomes [15,15,15,9,10,10,10]
"""

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0]*n

    # handle the first k indexes differently
    for j in range(k): dp[j]=max(arr[:j+1])*(j+1)

    # we can get rid of index i by running i times
    for j in range(k,n):
        curr = []
        for m in range(k):
            curr.append(dp[j-m-1] + max(arr[(j-m):(j+1)]) * (m+1))
            dp[j] = max(curr)
    return dp[-1]

if __name__=='__main__':
    print(maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))
