n=len(s1)
m=len(s2)

dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            dp[i][j]=0

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])


s=[]
i,j=n,m 
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        s.append(s1[i-1])
        j-=1
        i-=1
    elif d[i][j-1] > dp[i-1][j]:
        s.append(s2[j-1])
        j-=1
    else:
        s.append(s1[i-1])
        i-=1

while i>0:
    s.append(s1[i-1])
    i-=1

while j>0:
    s.append(s2[j-1])
    j-=1

scs=''.join(reversed(s))
return scs


