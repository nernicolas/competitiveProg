# This is a sample Python script.

import math
#import numpy as np

# Press Maj+F10 to execute it or replace it with your code.

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    b = [1 if i == 0 else -1 for i in arr]
    summ=0
    best=0
    cpt= 0
    indices=[]
    print(b)
    for k in range(n):
        summ = max(b[k], summ + b[k])
        best = max(best,summ)
        if(summ!= b[k]):
            indices.append(k-1)
            indices.append(k)
    indices = list(set(indices))
    print(indices)
    for i in indices:
        arr[i] = 1 - arr[i]
    print(best)
    print(arr)
    print(sum(arr))
    #print(best)
    """
    #solution using variation of maximal sum subsequence <=
    n = int(input())
    arr = [int(x) for x in input().split()]
    b =[ 1 if i ==0 else -1 for i in arr]
    msis = [1] * n
    cpt=0
    print(b)
    indices=[]
    for k in range(n):
        msis[k] = b[k]
        if arr[k]==1:
            cpt+=1
    for k in range(1,n):
        for i in range(k):
            if (b[i] <= b[k] and msis[k]<= msis[i] + b[k]):
                msis[k] = msis[i] + b[k]
                indices.append(i)
                indices.append(k)
                print(msis)

    indices = list(set(indices))
    indices.sort()
    print(indices)
    if(len(indices) > 1):
        for x in arr[indices[0]:indices[-1]]:
            if x==1:
                cpt-=1
    print(max(msis)+cpt)
    """
    """" brutal solution n**3
    #print(arr[0:2])

    cn=[]
    for i in range(n):
        for j in range(i,n):
            cnt = 0
            for k in range(n):
                if i<=k and k<=j:
                    cnt+= 1 - arr[k]
                else:
                    cnt+= arr[k]
            cn.append(cnt)

    print(max(cn))
    """
    """ longest increasing subsequence dp
    length=[0]*n
    for k in range(n):
        length[k] = 1;
        for i in range(k):
            if (arr[i] < arr[k]):
                length[k] = max(length[k], length[i]+1)
    print(max(length))
    """
    """ maximal sum subsequence dp
    n = int(input())
    arr = [int(x) for x in input().split()]
    msis = [0] * n
    for k in range(n):
        msis[k] = arr[k]
    for k in range(1, n):
        for i in range(k):
            if (arr[i] < arr[k] and msis[k] < msis[i] + arr[k]): ce bout la du if permet de s'assurer qu'on calcule la 
                                                                    somme maximale de la subsequence 
                                                                    et pas la somme de la subsequence la plus longue.
                                                                    en jouant avec les <=,==,>. on peut changer aller vers une decroissante
                                                                    etc
                msis[k] = msis[i] + arr[k]
    print(max(msis))
    """
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
