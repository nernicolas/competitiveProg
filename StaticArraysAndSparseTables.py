import math

def main():
    n = int(input())
    a = list(map(int,input().split()))
    l,r = map(int,input().split())

    def static_array(a): #precompute in 0(n) static array for sum queries in 0(1)
        stat = [0]*n
        stat[0]=a[0]
        for i in range(1,n):
            stat[i]=a[i]+stat[i-1]
        return stat

    def sum_range(arr,a,b): #compute sum(a,b) in O(1), using sum(a,b) = sum(0,b)+sum(0,a-1)
        if a!=0:
            return arr[b] - arr[a-1]
        else:
            return arr[b]

    def sparse_table(arr): #builds table in n*log(n) to answer min or max queries in 0(1)
        tab = [[0 for i in range(100)] for j in range(100)]
        n = len(arr)
        #preprocessing for k=0
        for i in range(n):
            tab[0][i] = a[i]
        k = 1
        #building table using values of layer k-1
        while (2 ** k <= n):
            i = 0
            while (i + 2 ** k - 1 < n):
                tab[k][i] = min(tab[k - 1][i], tab[k - 1][i + 2 ** (k - 1)])
                i += 1
            k += 1
        return tab

    def min_range(sparse_tab,a,b):
        length = b - a + 1
        k = math.floor(math.log2(length))
        ans = min(sparse_tab[k][a], sparse_tab[k][b - 2 ** k + 1])
        return ans

    arr = static_array(a)
    sparse = sparse_table(a)
    res1 = sum_range(arr, l, r)
    res2 = min_range(sparse,l,r)
    print(res1,res2)

if __name__ == '__main__':
    main()

