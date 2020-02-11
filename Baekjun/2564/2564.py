'''
1북 : x,0
2남 : x,100
3서 : 0,y
4동 : 100,y

왼쪽 : x1+x2 오른쪽 : (w+h) - (x1+x2)
위쪽 : y1+y2 아래쪽 : (w+h) - (y1+y2)
'''
def cal(d):
    if d[0][0] == d[1][0]:
        return abs(d[0][1] - d[1][1])
    if d[0][0] == 1 and (d[1][0] == 3 or d[1][0] == 4):
        return (d[0][1]+d[1][1]) if d[1][0] == 3 else (w-d[0][1]+d[1][1])
    
    if d[0][0] == 2 and (d[1][0] == 3 or d[1][0] == 4):
        return (h+d[0][1]-d[1][1]) if d[1][0] == 3 else ((w+h)-d[0][1]-d[1][1])

    if d[0][0] == 1 or d[0][0] == 2:
        return (h+d[0][1]+d[1][1]) if d[0][1]+d[1][1] <= w else ((w+h)-d[0][1]-d[1][1])
    
    if d[0][0] == 3 and (d[1][0] == 1 or d[1][0] == 2):
        return (d[0][1]+d[1][1]) if d[1][0] == 1 else (h+d[0][1]-d[1][1])
    
    if d[0][0] == 4 and (d[1][0] == 1 or d[1][0] == 2):
        return (w-d[0][1]+d[1][1]) if d[1][0] == 1 else ((w+h)-d[0][1]-d[1][1])
        
    if d[0][0] == 3 or d[0][0] == 4:
        return (w+d[0][1]+d[1][1]) if d[0][1]+d[1][1] <= h else ((w+h)-d[0][1]-d[1][1])
    
    if d[0][0] == 3 or d[0][0] == 4:
        return (h+d[0][1]+d[1][1]) if d[0][1]+d[1][1] <= h else ((w+h)-d[0][1]-d[1][1])

w, h = map(int, input().split())
N = int(input())
d = [[0,0]]
for i in range(N):
    d.append(list(map(int, input().split())))
d[0] = list(map(int, input().split()))

res = 0
for i in range(1, N+1):
    res += cal([d[0]]+[d[i]])
print(res)