import sys, threading


def main():
    n, k = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    res = []
    def dfs(s,e,depth):
        #process when arrives at node s
        count=1
        for u in adj[s]:
            if u != e:
                #process when considering a child from node s
                count+= dfs(u,s,depth+1)
                #process when coming back to last iteration of dfs
            #process even for visited node
        #process for all node when dfs is complete
        res.append(depth - count)

        return count

    dfs(0,-1,1)
    print(sum(sorted(res,reverse=True)[:k]))



if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(10 ** 8)
    t = threading.Thread(target=main)
    t.start()
    t.join()
