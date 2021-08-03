import math

def operation(n):
    return n-1 if n&(n-1) == 0 else n&operation(n-1)


def setBitNumber(n):
    # To find the position of
    # the most significant
    # set bit
    k = int(math.log2(n))

    # To return the value
    # of the number with set
    # bit at k-th position
    return 1 << k # or 2**k

def solve_iter(n):
    res = n
    k = n - 1
    while (k != 0):
        res &= k
        if res == 0:
            return k
        else:
            k -= 1

def main():
    #print(solve_iter(int(input())))
    #print(operation(int(input())))
    print(setBitNumber(int(input())) - 1)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        main()