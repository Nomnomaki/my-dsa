graph=defaultdict(list)
# k is source
for u,v,t in times:
    graph[u].append((v,t))

min_times={}
min_heap=[(0,k)] # time k to i, i 

while min_heap:
    time1, i=heapq.heappop(min_heap)
    if i in min_times:
        continue

    min_times[i]=time1
    for nn,nn_t in graph[i]:
        if nn not in min_times:
            heapq.heappush(min_heap,(time1+nn_t, nn))

if len(min_times)==n:
    return max(min_times.values())
else:
    return -1
