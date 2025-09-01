# same logic and code for min no of insertion to make a palindromic string

class Solution:
    def minDeletions(self, s):
        # code here
        temp=s[::-1]
        n=len(s)
        dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                dp[i][j]=0
                
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==temp[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
        
        cnt=dp[n][n]
        return n-cnt