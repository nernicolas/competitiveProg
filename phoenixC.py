import math
import heapq as hq



def main():
    n,m, x = map(int,input().split())
    a = list(map(int,input().split()))
    tower_set = [(0,i) for i in range(m)]
    hq.heapify(tower_set)
    order =[0]*n
    for i in range(n):
        tower = hq.heappop(tower_set)
        h=a[i]+ tower[0]
        order[i]=tower[1]+1
        hq.heappush(tower_set, (h,tower[1]))
    print("YES")
    print(' '.join(map(str,order)))





if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()

