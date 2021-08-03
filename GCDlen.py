import math


def main():
    a,b , c = map(int,input().split())
    x = 10**(a-1)
    y = 10**(b-1) + 10**(c-1) #we want x y that satisfies len(gcd(x,y))=c, if we have c 1 all we have to do is have 1
                                #power of 10 difference between x and y, and add 10**1 to y, to make it so
                                # that either the rest of y/x is the gcd, or if it's round then the gcd has len =c (1)
                                # instead of iterating on values and calculate a gcd each time, we just build one that works
                                # specific constraints lowers the size of subset of potential answers, so we extend the
                                # search few elements in a vast space. Prefer thinking about a solution that builds
                                # a solution over one that would iterate to find a solution for that kind of problem.
                                # 2 lines vs 30


    print(x," ",y)
    print(math.gcd(11,2))

    def gcd(x,y):
        while(y):
            x,y =y,x%y
            print(x,y)
        return x
    return

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()