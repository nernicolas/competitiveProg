# This is a sample Python script.

import math
#import numpy as np

# Press Maj+F10 to execute it or replace it with your code.

def main():
    n , K = map(int,input().split())
    h = [int(x) for x in input().split()]
    dp=[math.inf]*(n)
    dp[0] = 0
    """frog 1 - Top Bottom version doesnt allow for upgrade on frog 2 when you can jump as far as K stones away.
    dp[1] = abs(h[1] - h[0])
    for i in range(2,n):
        cost_1 = abs(h[i] - h[i-1])
        cost_2 = abs(h[i] - h[i-2])
        dp[i] = min(dp[i-1]+cost_1, dp[i-2]+cost_2)
    """
    indices = [] #used to keep track of the stones the frogs used as his path.
    for i in range(0,n):
        for j in range(i+1,i+K+1):  #can jump K stones
            if(j<n):
                if (dp[j] > dp[i] + abs(h[i] - h[j])): #if theres an update on dp[j], i is the stones on the optimal path
                    indices.append(i)
                dp[j] = min(dp[j],dp[i] + abs(h[i] - h[j]))
    indices.append(n-1)
    indices = list(set(indices))
    print(indices)
    print(dp[-1])

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
