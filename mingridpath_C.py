import math


def main():
    n = int(input())
    c = list(map(int, input().split()))
    mins = [math.inf]*2
    reminders = [n]*2
    summ=0
    ans = math.inf
    for i in range(n):
        mins[i%2] = min(mins[i%2], c[i])
        reminders[i%2]-=1
        summ +=c[i]
        ans = min(ans, summ+ reminders[0]*mins[0] + reminders[1]*mins[1])
        print(ans)
    print(ans)





if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
