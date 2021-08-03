import math

def main():
    n = int(input())
    adj = [[] for i in range(n)]
    for i in range(n-1):
        a , b= map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    visited = [False] * n
    mem_removed=[]

    def dfs(node,p=-1):
        c=0
        print("node entering dfs",node+1)
        print("node parent", p+1)
        if visited[node]:
            return
        else:
            visited[node]=True

        for el in adj[node]:
            if el != p:
                c+=1
                print("node calling dfs on child", node+1, el+1)
                dfs(el,p=node)
        print("node ending dfs",node+1)
        print("node parent", p + 1)
        print("c", c)
        if c ==2 and p!=-1:
            print("hey")
            mem_removed.append([node+1,p+1])

    def leaf(node,p, leafs=[]):
        flag= 1
        if visited[node]:
            return
        else:
            visited[node]=True

        for child in adj[node]:
            if node != p :
                flag=0
                leaf(child,node)
        if flag ==1:
            leafs.append(node)
        return leafs



    dfs(0)
    print(visited)
    print(adj)
    print(mem_removed)
    visited = [False]*n
    print(leaf(0,0))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
