# This is a sample Python script.
import cmath

# Press Maj+F10 to execute it or replace it with your code.

def main():
    n = int(input())
    bills = {1, 5, 10, 20, 100}
    value = []

    def solve_iter(n):
        value[0] = 0
        for x in range(1, n):
            value[x] = cmath.inf
            for b in bills:
                if (x - b >= 0):
                    value[x] = min(value[x], value[x - b] + 1)
            best = value[x]
        return best

    res = solve_iter(n)
    print(res)
    return

    """ greedy approach, can be generalized, works here because each value in the bills set can be divided by its predecessor
    a = n//100
    b = n%100//20
    c = n%100%20//10
    d = n%100%20%10//5
    e = n%100%20%10%5/1
    print(int(sum([a,b,d,c,e])))
    """
    """ dynammic programming recursively for coin like problems
    def solve(x):
        if x == 0:
            return 0
        if x < 0:
            return cmath.inf
        if ready[x - 1]:
            return value[x - 1]
        best = cmath.inf
        for b in bills:
            best = min(best, solve(x - b) + 1)
        ready[x - 1] = True
        value[x - 1] = best
        return best
    #we can also construct the value array iteratively, it's clearer but it's often easier to think about dp recursively
    """
        
    """
    res=[]
    obj=n
    l_bills = list(bills)
    l_bills.sort(reverse=True)
    for b in l_bills:
        res.append(obj//b)
        obj = obj%b
    print(sum(res))
    return
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
