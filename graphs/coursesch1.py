g=defaultdict(list)

courses=pre
for a,b in courses:
    g[a].append(b)

unvisited,visiting,visited=0,1,2

states=[unvisited]*nums

def dfs(node):
    state=states[node]
    if state==visited: return True
    elif state==visiting: return False

    states[node]=visiting
    for n in g[node]:
        if not dfs(n):
            return False

    states[node]=visited
    return True

for i in range(nums):
    if not dfs(i):
        return False
return True