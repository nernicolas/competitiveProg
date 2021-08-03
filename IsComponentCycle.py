
import sys, threading
def main():
    n,m = map(int,input().split())
    adj=[[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    #print(adj)
    visited = [False]*n
    if(n<3):
        print(0)
        return



    def dfs(s,p):
        #print("current",s,"previous",p)
        par=0
        if not visited[s]:
            visited[s]=True
        for u in adj[s]:
            par+=1
            if not visited[u]:
                dfs(u,s)
        if par==2:
            #print("hey")
            tab.append(True)
        else:
            tab.append(False)
        #print(tab)
        return tab

    n_comp=0
    n_comp_cycle=0
    while not all(visited):
        for i in range(n):
            tab=[]
            if not visited[i]:
                n_comp_cycle+=all(dfs(i,-1))
               # print(visited)
               # print("n_comp_cycle",n_comp_cycle)
                n_comp+=1

    #print(visited)
    #print(n_comp)
    print(n_comp_cycle)
    return

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(10 ** 8)
    t = threading.Thread(target=main)
    t.start()
    t.join()

