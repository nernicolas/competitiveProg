

def main():
    n = int(input())
    speed = list(map(int,input().split()))
    speed = list(sorted(speed))
    dp = [0]*n
    dp[0]=0
    for l in range(1,n):
        for i in range(n-l):
            dp[i]= speed[i+l]- speed[i] + min(dp[i],dp[i+1]) #here dp[i] has been calculated with l-1 at this stage
                                                            #so we choose here the best way to choose runners,
                                                            #by adding the sum and looking back which runners partitions
                                                            #was minimal at length l-1 so we can keeep going.

                                                            # saves memory for tab dp that could be built like dp[l][r]
    print(dp[0])

    return
if __name__ == '__main__':
    main()

