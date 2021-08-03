import math
from collections import deque
import heapq

def main():
    n, m, k = map(int,input().split())
    if k<=0:
        print(-1)
        return
    adj=[[] for i in range(n)]
    for i in range(m):
        a,b ,w = map(int,input().split())
        adj[a-1].append((b-1,w))
        adj[b-1].append((a-1,w))
    storage = list(map(int,input().split()))
    for i in range(k):
        storage[i]-=1
    storage=set(storage)

    def solve():
        res = math.inf
        for s in storage:
            for node,w in adj[s]:
                if node not in storage:
                    res = min(res,w)

        return res
    res = solve()
    if(res ==math.inf):
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    main()
