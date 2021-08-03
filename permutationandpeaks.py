import itertools

def main():
    n, k = map(int,input().split())

    def permutation(lst):

        # If lst is empty then there are no permutations
        if len(lst) == 0:
            return []

        # If there is only one element in lst then, only
        # one permuatation is possible
        if len(lst) == 1:
            return [lst]

        # Find the permutations for lst if there are
        # more than 1 characters

        l = []  # empty list that will store current permutation

        # Iterate the input(lst) and calculate the permutation
        for i in range(len(lst)):
            m = lst[i]

            # Extract lst[i] or m from the list.  remLst is
            # remaining list
            remLst = lst[:i] + lst[i + 1:]

            # Generating all permutations where m is first
            # element
            for p in permutation(remLst):
                l.append([m] + p)
        print(l)
        return l

    lis = [i+1 for i in range(n)]
    res = permutation(lis)
    if len(res)==1:
        print(res[0][0])
    else:
        for pe in res:
            peaks=0
            for i in range(1,n-1):
                if pe[i]>pe[i-1] and pe[i]>pe[i+1]:
                    peaks += 1
                    if peaks == k:
                        print(" ".join(str(x) for x in pe))
                        return
        print(-1)








if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
