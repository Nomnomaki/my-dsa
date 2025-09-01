if not node:
    return None

start=node
visited=set()
visited.add(start)
stk=[]
stk.append(start)
o_to_n={}


while stk:
    node=stk.pop()
    o_to_n[node]=Node(val=node.val)

    for nn in node.neigbors:
        if nn not in visited:
            visited.add(nn)
            stk.append(nn)


for old, new in o_to_n.items():
    for nn in old.neighbors:
        new_nn=o_to_n[nn]
        new.neighbors.append(new_nn)

return o_to_n[start]
