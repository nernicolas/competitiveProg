
def main():
    adj = [[] for i in range(7)]
    adj[0].append(1)
    adj[0].append(3)
    adj[0].append(2)
    adj[1].append(5)
    adj[1].append(0)
    adj[1].append(4)
    adj[2].append(0)
    adj[3].append(6)
    adj[3].append(0)
    adj[4].append(0)
    adj[5].append(1)
    adj[6].append(3)
    leaf=[0]*7
    maxlen = [0]*7
    visited = [False]*7
    def dfs(s,e):
        print(s, e)
        if not visited[s]:
            visited[s]=True
        for u in adj[s]:
            if visited[u]:
                continue
            dfs(u, s)
            leaf[s] = max(leaf[s],leaf[u]+1)
            for k in adj[s]:
                if(k!=u):
                    maxlen[s] = max(maxlen[s], leaf[u]+leaf[k])
        maxlen[s]+=2

    dfs(0,0)
    print(leaf[0])
    print(maxlen[0])

if __name__ == '__main__':
        main()
