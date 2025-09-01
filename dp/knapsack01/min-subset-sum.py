def isSubSetSum(self,arr,summ) -> List:
    n=len(arr)
    dp=[[False for _ in range(summ+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]


    res = [j for j in range(summ + 1) if dp[n][j]]

    return res  

def minimumDifference(self, nums: List[int]) -> int:
    temp = self.isSubSetSum(nums, yoo)
    m=len(temp)
    minn=float('inf')
    for i in range(m):
        minn=min(minn,yoo-2*temp[i])

    return minn


# from typing import List

# class Solution:
#     def isSubSetSum(self, arr, summ) -> List[int]:
#         n = len(arr)
#         if n == 0:
#             return [0] if summ == 0 else []
        
#         dp = [[False for _ in range(summ + 1)] for _ in range(n + 1)]
#         for i in range(n + 1):
#             dp[i][0] = True  

#         for i in range(1, n + 1):
#             for j in range(summ + 1):
#                 if j >= arr[i - 1]:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
#                 else:
#                     dp[i][j] = dp[i - 1][j]

#         return [j for j in range(summ + 1) if dp[n][j]]

#     def minDifference(self, arr: List[int]) -> int:
#         if not arr:
#             return 0

#         total = sum(arr)
#         possible_sums = self.isSubSetSum(arr, abs(total))  
#         min_diff = float('inf')

#         for s in possible_sums:
#             if s <= total // 2:
#                 min_diff = min(min_diff, abs(total - 2 * s))  

#         return min_diff

