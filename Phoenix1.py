import math




def main():
    n ,x= map(int,input().split())
    a = list(map(int,input().split()))
    order = [0]*n
    if sum(a) ==x:
        print("NO")
    else:
        cpt=0
        for i in range(n):
            cpt+=a[i]
            if cpt ==x:
                cpt-=a[i]
                cpt+=a[i+1]
                a[i+1],a[i] = a[i],a[i+1]
        print("YES")
        for i in range(n):
            print(a[i],end=" ")








if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()

