res,sol=[],[]
n=len(nums)

def backtrack():
    if len(sol)==n:
        res.append(sol[:])
        return 
    
    for x in nums:
        if x not in sol:
            sol.append(x)
            backtrack()
            sol.pop()

backtrack()
print(res)