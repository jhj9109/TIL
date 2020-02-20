import math

def rsp(cards, a, b):
    if (cards[a]==1 and cards[b]==2) or (cards[a]==2 and cards[b]==3) or (cards[a]==3 and cards[b]==1):
        return b
    else: return a
    

def tour(cards, start, end):
    if len(cards[start:end]) > 2:
        half = math.ceil((start+end)/2)
        w1 = tour(cards, start, half)
        w2 = tour(cards, half, end)
        return rsp(cards, w1, w2)
    else:
        if len(cards[start:end]) == 2:
            return rsp(cards, start, start+1)
        elif len(cards[start:end]) == 1:
            return start

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    card = list(map(int, input().split()))
    winner = tour(card, 0, num)
    print(f'#{tc} {winner+1}')
