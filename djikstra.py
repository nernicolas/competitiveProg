import math
import heapq
def main():
    n, m = map(int,input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        a,b,w = map(int,input().split())
        adj[a-1].append((b-1,w))
        adj[b-1].append((a-1,w))


    def djikstra(x,end):
        n=len(adj)
        visited = [False] * n
        path = []
        distances = [math.inf] * n
        distances[x] = 0
        pre=[-1]*n
        pq = list()
        heapq.heapify(pq)
        heapq.heappush(pq,(0,x)) # (-d,x) where d is distances

        while(pq):
            distance,node = heapq.heappop(pq) #take the node not the distance
            for next in adj[node]:
                el = next[0]
                w = next[1]
                if distances[node] + w < distances[el]:
                    pre[el]=node
                    distances[el] = distances[node] + w
                    heapq.heappush(pq,(distances[el],el))
        if pre[end]==-1:
            print("-1")
        else:
            v=end
            while(v != -1):
                path.append(pre[v])
                v = pre[v]
            path.reverse()
            path.append(end)
            path = [str(el+1) for el in path if el!= -1]
            print(" ".join(path))

    djikstra(0,n-1)




if __name__ == '__main__':
    main()
