import sys
input = sys.stdin.readline().strip
sys.stdin = open('input.txt') #readline은 스트링인풋을 받을때, 줄바꿈 캐릭터를 없애 줘야한다. >>strip

T = int(input())

for tc in range(1, T+1):
    d = input()
    s = []
    for c in d:
        if c == '(':
            s.append(c)
        else:
            if not len(s):
                print('NO')
                break
    else:
        if not len(s):
            print('YES')
        else:
            print('NO')