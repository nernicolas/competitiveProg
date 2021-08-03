# This is a sample Python script.

import math
#import numpy as np

# Press Maj+F10 to execute it or replace it with your code.

def main():
    n = int(input())
    shops = [int(x) for x in input().split()]
    q = int(input())
    m = max(shops)
    dp=[0] * (m +1)
    for i in shops:
        dp[i]+=1
    for i in range(1,m+1):
        dp[i] += dp[i-1]
    for i in range(q):
        print(dp[min(m,int(input()))])

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
