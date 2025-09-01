class Solution:
    def isSubSet(self,arr,summ) -> bool:
            n=len(arr)
            dp = [[False for _ in range(summ + 1)] for _ in range(n + 1)]
            for i in range(n+1):
                dp[i][0]=True
            
            for i in range(1,n+1):
                for j in range(summ+1):
                    if arr[i-1]<=j:
                        dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    else:
                        dp[i][j]=dp[i-1][j]
            return dp[n][summ]
                

    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2==0:
            return self.isSubSet(nums,summ//2)
        else:
            return False
       
        
    