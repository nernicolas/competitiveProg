import math


def main():
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    adj = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    visited = [False] * n
    def dfs(s):
        stack = list()
        stack.append(s)
        c=math.inf  #be careful with large numbers in tuple , either use arguments in dfs function or stack, or build wrap
                    #wrap function around dfs with proper args
        while(stack):
            s =stack.pop()
            c = min(c, arr[s])
            if not visited[s]:
                visited[s]=True
            for u in adj[s]:
                if not visited[u]:
                    stack.append(u)
        return c

    summ = 0
    for i in range(n):
        if not visited[i]:
            summ+= dfs(i)
    print(summ)


if __name__ == '__main__':
    main()