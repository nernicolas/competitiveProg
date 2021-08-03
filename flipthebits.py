
def main():
    t = int(input())
    while(t!=0):
        n=int(input())
        a = [ int(x) for x in input()]
        b=  [int(x) for x in input()]
        tag=True
        sum=0
        for i in range(n):
            sum+=a[i]
            if(i<n-1):
                if(((a[i]==b[i] and a[i+1]!=b[i+1]) or (a[i]!=b[i] and a[i+1]==b[i+1]))):
                    if sum!= ((i+1)/2):
                        tag=False
                        break
            else:
                if(a[i]!=b[i]):
                    if sum != ((i+1) /2):
                        tag = False
                        break

        if tag:
            print('YES')
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    main()
