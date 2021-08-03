import math

def main():
    n = int(input())
    a = list(map(int,input().split()))
    l,r = map(int,input().split())
    power2 = {2**x for x in range(32)}
    #segment tree for computing range queries in 0(logn) , constructing the tree is O(n)
    def stree(a):
        n = len(a)
        if n not in power2:
            return
        else:
            tree = [0] *(2*n) # 2n elements so we can use tree[0]=0 to simulate indexing starting at 1, important to see which node is child or parent of another node
                            # we ll use rules as tree[k//2] is parent node , and tree[2k] and tree[2k+1] is child nodes
            #we build tree array with values of a, starting at index n till 2n (excluded) for tree array so n elements
            for i in range(n,2*n):
                tree[i] = a[i-n]
            #we construct the rest of the array using child values
            for i in range(n-1,0,-1):
                tree[i] = tree[2*i] + tree[2*i+1]
        print(tree)
        return tree

    def sum_range_st(tree, a,b):
        a += n
        b+=n
        s = 0
        while(a<=b):
            if a % 2 == 1:
                s += tree[a]
                a+=1
            if b%2 ==0:
                s+= tree[b]
                b-=1
            a = a // 2
            b = b //2
        return s

    def add_st(tree, k, x): #function to update an element of the array by adding a value to it , while updating the entire seg tree
        k+=n
        tree[k] +=x
        k = k//2
        while(k>0):
            tree[k] = tree[2*k] + tree[2*k+1]
            k = k//2
        return tree

    st = stree(a)
    print(sum_range_st(st, 0,2))

    print(add_st(st, 0,2))


if __name__ == '__main__':
    main()

