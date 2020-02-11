import sys
sys.stdin = open('input.txt')

K = int(input())
s=[[0] for _ in range(4)]
comp = [1,0,3,2]
# print(s[0])
# print(s[0][0])
i = []
for _ in range (6):
    n, l = map(int, input().split())
    n -= 1  
    if s[n][0] == 0:
        s[n][0] = l
    else:
        s[n].append(l)
        i.append(n)
res = s[comp[i[0]]][0]*s[comp[i[1]]][0] - s[i[0]][1]*s[i[1]][0]
print(res * K)