

def crible_erathostene(n):
    prime = [True for i in range(n + 1)]
    prime_list=set()
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            prime_list.add(p)
    return prime_list


def main():
    n = int(input())
    arr = list(map(int,input().split()))
    primes = set(crible_erathostene(1000000))
    T_primes = [x**2 for x in primes]
    for el in arr:
        if el in T_primes:
            print('YES')
        else:
            print('NO')






if __name__=='__main__':
        main()