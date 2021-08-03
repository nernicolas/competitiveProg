import math
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    cpt=0
    r = [0]*n
    c = [0]*3
    for i in range(n):
        c[arr[i]%3]+=1
        r[i] = arr[i]%3
    while(not(c[0]==c[1] and c[1]==c[2])):
        k = c.index(max(c))
        j = r.index(k)
        arr[j]+=1
        r[j] = arr[j]%3
        c[r[j]] +=1
        c[k]-=1
        cpt += 1
    print(cpt)
    return

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
