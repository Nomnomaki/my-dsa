# recursive

 def lcs(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1+lcs(x,y,n-1,m-1)
    else:
        return max(lcs(x,y,n-1,m), lcs(x,y,n,m-1))

# memo

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        def lcs(n, m):
            if n == 0 or m == 0:
                return 0
            if dp[n][m] != -1:
                return dp[n][m]
            if text1[n - 1] == text2[m - 1]:
                dp[n][m] = 1 + lcs(n - 1, m - 1)
            else:
                dp[n][m] = max(lcs(n - 1, m), lcs(n, m - 1))
            return dp[n][m]

        return lcs(n, m)

# top down

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]