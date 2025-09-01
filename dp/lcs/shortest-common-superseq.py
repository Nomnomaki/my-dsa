n=len(s1)
m=len(s2)
def lcs(s1,s2,n,m):
    dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[n-1]==s2[m-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

return (m+n)-lcs(s1,s2,n,m)