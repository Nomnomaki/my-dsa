class Solution:
    def subsetSum(self,nums,target):
        n=len(nums)
        dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        
        for i in range(1,n+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        goal=(target+total)//2

        return self.subsetSum(nums,goal)
        