import math
def is_palindrom(s):
    return True if s[::-1]==s else False

def play_turn(s,n, last_reverse=False):
    for i in range(n):
        if s[i]=='0' and is_palindrom(s[0:i] + '1' + s[i+ 1:]) and s[0:i] + '1' + s[i+ 1:] != '1'*n:

            s = s[0:i] + '1' + s[i+ 1:]
            return s,last_reverse,1
    if not is_palindrom(s) and not last_reverse:
        last_reverse = True
        #print("String has been reversed")
        s = s[::-1]
        return s, last_reverse, 0
    else:
        any_0 = s.find('0')
        s = s = s[0:any_0] + '1' + s[any_0+ 1:]
        return s, last_reverse, 1

def simulate(s,n):
    alice, bob = 0, 0
    res_s = s
    last_reverse = False
    i = 1
    while (res_s != '1' * n):
        if i % 2 != 0:
            res_s, last_reverse, cost = play_turn(res_s, n, last_reverse)
            alice += cost
            # print("Alice played " ,res_s)
        else:
            res_s, last_reverse, cost = play_turn(res_s, n, last_reverse)
            bob += cost
            # print("BOB played ",res_s)
        i += 1

    if alice > bob:
        print("BOB")
    elif alice < bob:
        print("ALICE")
    else:
        print("DRAW")

def solve(s):
    count_0 = s.count('0')
    if count_0 %2 ==0:
        print("BOB")
    elif count_0 %2 !=0 and count_0 != 1:
        print('ALICE')
    elif count_0 == 1:
        print('BOB')

def main():
    n = int(input())
    s = input()
    #simulate(s,n)
    solve(s)





if __name__=='__main__':
    t = int(input())
    for i in range(t):
        main()