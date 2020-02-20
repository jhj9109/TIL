import sys
sys.stdin = open('input.txt')

T=int(input())

di=[1,0,-1,0]
dj=[0,1,0,-1]

def dfs(i,j):
    if maze[i][j]==3:
        return 1
    else:
        maze[i][j]=1
        for k in range(4):
            ni = i + di[k]    
            nj = j + dj[k]
            if maze[ni][nj] !=1:
                if dfs(ni,nj)==1:
                    return 1
        return 0

for tc in range(1,T+1):
    N= int(input())
    wall=[[1]*(N+2)]
    maze=wall+ [[1]+list(map(int, list(input())))+[1] for _  in range(N)] + wall

    #visited= [[0]*(N+2) for _ in range(N+2)]
    
    for i in range(N+2):
        for j in range(N+2):
            if maze[i][j]==2:
                si=i
                sj=j
                break
    print('#{} {}'.format(tc, dfs(si,sj)))


