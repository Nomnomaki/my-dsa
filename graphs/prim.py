n=len(points)   
cost=0
seen=set()
min_heap=[(0,0)]

while len(seen)<n:
    dist, i = heapq.heappop(min_heap)
    if i in seen:
        continue
    seen.add(i)
    cost+=dist 
    xi,yi=points[i]

    for j in range(n):
        if j not in seen:
            xj,yj=points[j]
            nn_dist=abs(xi-xj)+abs(yi-yj)
            heapq.heappush(min_heap, (nn_dist,j))

return cost 
