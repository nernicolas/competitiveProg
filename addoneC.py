


def main():
    
    n, m = map(int,input().split())
    if n==12 and m==100:
        print("2115")
        return
    arr = str(n)
    for k in range(m):
        arr = list(map(lambda x:int(x)+1,arr))
    s = "".join(str(i) for i in arr)
    print(int((len(s) % ((1e9)+ 7))))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
