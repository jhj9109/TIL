V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [ [0] * (V+1) for _ in range(V+1)] #인접행렬
for i in range(E):
    adj[edge[i * 2]][edge[i * 2 + 1]]
    #아래는 무방향그래프에만 추가된다.
    adj[edge[i * 2 + 1]][edge[i * 2]]

dfs1(1, V)

def dfs1(v, V):
    visited[v] = 1
    print(v, end = ' ')
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs1(w)

def dfs2(n, V):
    q = []
    q.append(n) #시작점을 push
    visited[n] = 1 #스택에 저장됨
    while len(s)>0: #스택에 방문할 노드(갈림ㅁ길0이 남아있지 않으면
        n = s.pop()
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: # n번 노드에서 갈수 있는 노트 i
                s.append(i)
                visited[i] = 1

def dfs3(n, v, V): #강사님 코드, 끝 점까지 탐색 끝났으면 종료되는 코드
    if n == t:
        return 1
    else:
        visited[n] = 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                if dfs1(i, V, t) == 1:  # i노드로 이동
                    return 1
            return 0  # dfs1이 1을 리턴한 적이 없으면(목적지를 방문하지 못하면)

def dfs4(n, V): #강사님 코드, 끝 점까지 탐색 끝났으면 종료되는 코드(반복버전)
    q = []
    q.append(n)  # 시작점을 push
    visited[n] = 1  # 스택에 저장됨
    while len(s) > 0:  # 스택에 방문할 노드(갈림ㅁ길0이 남아있지 않으면
        n = s.pop()
        if n == t:
            return 1

        for i in range(1, V + 1):
            if adj[n][i] == 1 and visited[i] == 0:  # n번 노드에서 갈수 있는 노트 i
                s.append(i)
                visited[i] = 1
    return 0