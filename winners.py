



def main():
    n= int(input())
    scores = dict()
    book = list()
    for i in range(n):
        name , score = input().split()
        scores[name] = scores.setdefault(name,0) + int(score)
        book.append([name,int(score)])
    m = max(scores.values())
    winners = dict()
    for k,v in scores.items():
        if v == m:
            winners.setdefault(k,0)
    for round in book:
        if round[0] in winners.keys():
            winners[round[0]] += round[1]
            if(winners[round[0]] >= m):
                print(round[0])
                break
    return

if __name__ == '__main__':
    main()
