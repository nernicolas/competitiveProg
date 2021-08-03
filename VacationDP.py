# This is a sample Python script.

import math
#import numpy as np

# Press Maj+F10 to execute it or replace it with your code.

def main():
    n = int(input())
    dp = [0]*3
    dp[0] = 0
    for i in range(n):
        nw_dp =[0]*3
        arr = list(map(int, input().split()))
        for j in range(3):
            for k in range(3):
                if j!=k:
                    nw_dp[j] = max(nw_dp[j], dp[k] + arr[j])
        dp =nw_dp
    print(max(dp))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
