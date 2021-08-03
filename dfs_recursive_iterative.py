from collections import deque
def main():
    n , t = map(int,input().split())
    adj_list = [[] for i in range(n)]
    visited = [False] * (n)
    a= list(map(int,input().split()))
    for i in range(len(adj_list)-1):
        adj_list[i].append(i+a[i])
    def dfs(node):
        if visited[node]:
            return
        else:
            visited[node]=True
            #process with node "node"
            for el in adj_list[node]:
                dfs(el)

    def dfs_iter(node):
        stack = []
        stack.append(node)

        while(len(stack) != 0 ):
            node =stack[-1]
            stack.pop()

            if not visited[node]:
                visited[node]=True

            for nodes in adj_list[node]:
                if not visited[nodes]:
                    stack.append(nodes)


    dfs(0)
    #dfs_iter(0)
    if(visited[t-1]):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
