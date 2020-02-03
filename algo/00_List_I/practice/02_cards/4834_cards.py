#import sys
#sys.stdin = open("sample_input2.txt", "r")

"""
T 반복
N 카드장수
test 카드N(붙어서)
가장 많은 카드, 갯수

T 받고
T 반복
N 받고
test 분류하고
test 돌면서 카운팅하고 (0~9미리준비한 카운터)
카운트중 가장 큰 값과 그 인덱스 저장 후 출력
"""

T = int(input())
for T in range(T):
    N = int(input())
    test = list(input())
    #test = [int(n) for n in str(input().strip())]
    
    counter = [0]*10
    counter[test[0]] += 1
    max_num = test[0]

    for num in test[1:]:
        counter[num] += 1
        if counter[num] > counter[max_num]:
            max_num = num
        if counter[num] == counter[max_num]:
            max_num = num if num > max_num else max_num
    print(f'#{T+1} {max_num} {counter[max_num]}')
'''
    max_num = 0
    max_cnt = 0
    for num in test[1:]:
        counter[num] += 1
    for i in range(10):
        if counter[i] >= max_cnt:
            max_cnt = counter[i]
            max_num = i



    print(f'#{T+1} {max_num} {counter[max_num]}')
'''


"""카운터 방식
from collections import Counter
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    d = list(input())
    c = Counter(d).most_common()
    print(f'Counter(d).most_common() : {c}')
    max_num = c[0][1]
    print(f'max_num : {max_num}')
    max_cards = [x for x, y in c if y == max_num]
    print(f'max_cards : {max_cards}')
    print(f'#{tc} {max(max_cards)} {max_num}')
"""