# This is a sample Python script.

import math


# Press Maj+F10 to execute it or replace it with your code.

def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    """
    dragons = [i for i in range(d)]
    hurt = [False for i in dragons]
    for el in [k, l, m, n]:
        for i in range(el-1,len(dragons),el):
            if not hurt[i]:
                hurt[i] = True
    nb = hurt.count(True)
    print(nb)
    """
    """
    #0(1) version (lcm not counted) using inclusion-exclusion principle 
    The idea here is that from 1 to D, there is d/k dragons hurted for reason k, and d/l for reason.
    in total there is sum(d/k,d/l) dragons hurted but maybe some of those dragons were hurted by the 2 reasons and thus,
    we have to substract those dragons. how to know how much of these dragons there are from 1 to D? 
    we can see that there are d/(k*l) dragons (if k=2,l=3 , then each 6-indices, we will have the dragon with the 2 reasons,
    so d/6)
    but actually d/lcm(k,l) is better as it will count each least_common_divisor_of_lk-indices.
    then we do N1-N2
    Now if we have more groups, we have to calculate till Ni, which is the number of dragons impacted by at least i-reasons.
    So to get thos Ni , we just use the inclusion of all the combinations of i reasons among the total r reasons. 
    so sum(d/lcm(C) for c in combinations((l,k,m),(l,k,m,n))) for r=4 and i=3 and we do this for all i.
    To get the total number of dragons, we just have to use the exclusion formula sum((-1)**k * Ni) k from 1 to R
    """
    n1 = d / k + d / l + d / m + d / n
    n2 = d / math.lcm(k, l) + d / math.lcm(k, m) + d / math.lcm(k, n) + d / math.lcm(l, m) + d / math.lcm(l,
                                                                                                          n) + d / math.lcm(
        m, n)
    n3 = d / math.lcm(k, l, m) + d / math.lcm(k, l, n) + d / math.lcm(m, l, n) + d / math.lcm(m, k, n)
    n4 = d / math.lcm(k, l, m, n)

    res = n1 - n2 + n3 - n4
    print(int(res))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
