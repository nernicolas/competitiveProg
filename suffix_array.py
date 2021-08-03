
def radix_sort(suffix):
    n = len(suffix)
    buckets = [[0, 0, 0] for i in range(n)]
    cpt=[0]*(n+1)
    pos = [0]*(n+1)
    for i in range(n):
        cpt[suffix[i][2]]+=1
    if cpt[-1] != 0:  #-1 exists in nxt_rank of suffixes, 0s should come after -1s
        pos[0] = pos[-1] + cpt[-1]
    for i in range(1,n):
        pos[i]= pos[i-1] + cpt[i-1]
    for ind,rank,nxt_rank in suffix:
        buckets[pos[nxt_rank]] = [ind,rank,nxt_rank]
        pos[nxt_rank]+=1

    suffix = buckets.copy()

    cpt = [0] *(n+1)
    pos = [0] * (n+1)
    for i in range(n):
        cpt[suffix[i][1]] += 1
    if cpt[-1] != 0:  # -1 exists in rank of suffixes, 0s should come after -1s
        pos[0] = pos[-1] + cpt[-1]
    for i in range(1,n):
        pos[i] = pos[i - 1] + cpt[i - 1]
    for ind, rank, nxt_rank in suffix:
        buckets[pos[rank]] = [ind, rank, nxt_rank]
        pos[rank] += 1

    return buckets



def main():
    s = input()
    s += '$'
    n = len(s)

    suffixes = [[0,0,0] for i in range(n)]
    for i in range(n):
        suffixes[i][0] = i
        suffixes[i][1] = (ord(s[i])- ord("a"))
        suffixes[i][2] = (ord(s[i+1]) - ord("a")) if i+1 < n else -1

    suffixes = sorted(suffixes,key = lambda x: tuple(x[1:])) # sorted by first two characters

    ind = [0]*n #ind[i] se refere a l'indice du suffixe ayant l'indice i
    k=4
    while(k< 2*n):
        rank = 0
        prev_rank = suffixes[0][1]
        suffixes[0][1] = rank
        ind[suffixes[0][0]]=0

        for i in range(1,n):
            if (suffixes[i][1]==prev_rank and suffixes[i][2] == suffixes[i-1][2]):
                prev_rank=suffixes[i][1]
                suffixes[i][1] = rank
            else:
                prev_rank = suffixes[i][1]
                rank+=1
                suffixes[i][1] = rank
            ind[suffixes[i][0]] = i

        for i in range(n):
            next_ind = suffixes[i][0] + k //2
            suffixes[i][2] = suffixes[ind[next_ind]][1] if next_ind < n else -1
        #suffixes = sorted(suffixes , key = lambda x : tuple(x[1:]))
        suffixes = radix_sort(suffixes)
        k*=2
    suffixes_res = [0]*n
    for i in range(n):
        suffixes_res[i] = suffixes[i][0]
    for i in range(n):
        print(suffixes_res[i],end=' ')

    return suffixes_res


    def sufar_n2(s):
        s +='$'
        sa = [0]*len(s)
        sa_f=[0]*len(s)
        for i in range(len(s)):
            sa[i]=s[i:]
        sa.sort()
        for i in range(len(s)):
            sa_f[i]=(len(s)-len(sa[i]))
        return sa_f



if __name__ == '__main__':
    main()

