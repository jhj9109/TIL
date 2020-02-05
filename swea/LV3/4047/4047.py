import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    flag = True
    
    cards = dict.fromkeys(['S', 'D', 'H', 'C'], 13)
    data = input().strip()

    datas = []
    for i in range(len(data)//3):
        datas.append(data[3*i: 3*i+3])
    #print(datas)
    #print(len(datas), len(set(datas)))

    if len(datas) != len(set(datas)) :
        print(f'#{tc} ERROR')
        flag = False

    if flag:
        for d in datas:
            #print(d[0])
            cards[d[0]] -= 1
        print(f'#{tc} ', end='')
        for v in cards.values():
            print(v, end=' ')
        print('')