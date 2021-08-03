import math

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    x = min(arr)
    j = arr.index(x)
    info=[]
    for i in range(n):
        if i != j:
            y=x+abs(j-i)
            info.append([j+1,i+1,x,y])
            arr[i]=y
    print(len(info))
    for i in range(len(info)):
        print(" ".join(map(str,info[i])))








if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
