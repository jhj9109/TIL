import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    length = [len(words[i]) for i in range(5)]
    n = 0 #most length
    for l in length:
        n = l if l > n else n
    result =''
    for i in range(n):
        for j in range(5):
            if i+1 <= length[j]:
                pass
                result += words[j][i]
    print(f'#{tc} {result}')

