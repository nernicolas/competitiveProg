# This is a sample Python script.

import math
#import numpy as np

# Press Maj+F10 to execute it or replace it with your code.

def main():
    s = input()
    n=len(s)
    m = int(input())
    A=[0]
    k=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            k+=1
        A.append(k)
        print(A)


    for i in range(m):
        l,r =[int(x) for x in input().split()]
        print(A[r-1] - A[l-1])
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
