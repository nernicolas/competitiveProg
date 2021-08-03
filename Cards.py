from collections import deque
from itertools import islice


def main():
    n, q = map(int,input().split())
    cards = deque(list(map(int,input().split())))

    queries = list(map(int,input().split()))
    for i in range(q):
        query = queries[i]
        print(cards.index(query,0,n)+1, end=" ")
        cards.remove(query)
        cards.appendleft(query)
    return

if __name__ == '__main__':
        main()
