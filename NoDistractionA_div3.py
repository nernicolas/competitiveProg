import math


def main():
    n= int(input())
    s = input()
    seen =[]
    for i in range(n):
        if s[i] not in seen:
            first_ai = s.find(s[i])
            last_ai = s.rfind(s[i])
            for j in range(first_ai+1,last_ai+1):
                if s[i] != s[j]:
                    print("NO")
                    return
        seen.append(s[i])
    print("YES")

    #better is
    """
    n = int(input())
    s = input()
    seen =set()
    for i in range(n):
        if (i>=1 and s[i-1]!=s[i] and s[i] in seen):
            return "NO"
        seen.add(s[i])
    return("YES)
    """
        




if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()
