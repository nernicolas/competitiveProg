import math
def get_digit(number, n):
    return number // 10**n % 10

def main():
    n=int(input())
    k=0
    res=0
    k=math.floor(math.log10(n))
    res = 9*k + get_digit(n,k) - 1
    if n >= int(str(get_digit(n,k))*(k+1)):
        res+=1
    print(res)







if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
