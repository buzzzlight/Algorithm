T = int(input())

for i in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    if N % 2 == 0:
        cards_1 = cards[0:N//2]
        cards_2 = cards[N//2:]
        cards_3 = []
        for j in range(N//2):
            cards_3.append(cards_1[j])
            cards_3.append(cards_2[j])
        print(f'#{i}', end=' ')
        print(*cards_3)
    else:
        cards_1 = cards[0:(N+1)//2]
        cards_2 = cards[(N+1)//2:]
        cards_3 = []
        for j in range((N+1)//2 - 1):
            cards_3.append(cards_1[j])
            cards_3.append(cards_2[j])
        cards_3.append(cards_1[-1])
        print(f'#{i}', end=' ')
        print(*cards_3)