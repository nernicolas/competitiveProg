
def main():
    s1 = input()
    s2= input()
    n=len(s1)
    m=len(s2)
    distance=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        distance[i][0]=i
    for j in range(m+1):
        distance[0][j] = j
    for a in range(1,n+1):
        for b in range(1,m+1):
            cost = 0 if s1[a-1]==s2[b-1] else 1
            distance[a][b]= min(distance[a][b-1]+1, distance[a-1][b]+1, distance[a-1][b-1] +cost)
    print(distance[n][m])
    for a in range(n+1):
        print(distance[a])

    return

if __name__ == '__main__':
    main()
