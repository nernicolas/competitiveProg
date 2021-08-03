
def main():
    n, m = map(int,input().split())
    vertices = list(map(int,input().split()))
    adj = [[] for i in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    n_rest=[]
    leaf = [0]*n
    for i in range(n):
        if i != 0 and len(adj[i])==1:
            leaf[i]=1

    def dfs(s, e,k=0,is_leaf=False):
        if vertices[s]:
            k+=1
        else:
            k=0
        if k > m:
            return
        is_leaf = True
        for child in adj[s]:
            if child != e:
                is_leaf = False
                dfs(child, s, k,is_leaf)
        if s!= 0 and is_leaf:
            n_rest.append(1)
            return

        return n_rest

    visited = [False]*n
    has_cat = [ x ==1 for x in vertices]
    def dfs_iter(s):
        stack=list()
        stack.append((s,-1,vertices[s]))
        cpt = 0
        while(len(stack) != 0 ):
            s,p, c =stack.pop()
            if c > m:
                continue
            leaf=True
            for child in adj[s]:
                if child != p:
                    leaf=False
                    stack.append((child,s,(c+1) if has_cat[child] else 0))
            if(leaf):
                cpt+=1

        return cpt


    #dfs(0,0)
    print(dfs_iter(0))
    #print(sum(n_rest))

if __name__ == '__main__':
    main()
