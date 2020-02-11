'''
1북 : x,0
2남 : x,100
3서 : 0,y
4동 : 100,y

왼쪽 : x1+x2 오른쪽 : 200 - (x1+x2)
위쪽 : y1+y2 아래쪽 : 200 - (y1+y2)
'''
def cal(d):
    if (d[0][0] == d[n][0]):
        return abs(d[0][1] - d[n][1])
    if d[0][0] == 1 and (d[n][0] == 3 or d[n][0] == 4):
        return (d[0][1]+d[n][1]) if d[n][0] == 3 else (100-d[0][1]+d[n][1])
    
    if d[0][0] == 2 and (d[n][0] == 3 or d[n][0] == 4):
        return (100+d[0][1]-d[n][1]) if d[n][0] == 3 else (200-d[0][1]-d[n][1])

    if d[0][0] == 1 or d[0][0] == 2:
        return (100+d[0][1]+d[n][1]) if d[0][1]+d[n][1] <= 100 else (200-d[0][1]-d[n][1])
    
    if d[0][0] == 3 and (d[n][0] == 1 or d[n][0] == 2):
        return (d[0][1]+d[n][1]) if d[n][0] == 1 else (100+d[0][1]-d[n][1])
    
    if d[0][0] == 4 and (d[n][0] == 1 or d[n][0] == 2):
        return (100-d[0][1]+d[n][1]) if d[n][0] == 1 else (200-d[0][1]-d[n][1])
        
    if d[0][0] == 1 or d[0][0] == 2:
        return (100+d[0][1]+d[n][1]) if d[0][1]+d[n][1] <= 100 else (200-d[0][1]-d[n][1])
    
    if d[0][0] == 3 or d[0][0] == 4:
        return (100+d[0][1]+d[n][1]) if d[0][1]+d[n][1] <= 100 else (200-d[0][1]-d[n][1])

w, h = map(int, input().split())
N = int(input())
d = [[0,0]]
for i in range(N):
    d.append(list(map(int, input().split())))
d[0] = list(map(int, input().split()))
for i in range(1, N+1):
    cal(d[0]+d[i])