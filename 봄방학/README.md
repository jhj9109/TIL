# # 봄방학

## 0226

- 6485 삼성시의 버스노선 : 이중포문 돌며 버스시점<= 정류장 <= 버스종점 : 카운팅

## 0227

- 1258 [S/W 문제해결 응용] 7일차 - 행렬찾기 : 영역 구분해 크기 저장, 출력전 정렬(itertools.itemgetter사용) or 저장하며 정렬(push pop 사용)

## 0228

- 1486 장훈이의 높은 선반 : itertools의 combinations(이터러블, 원소갯수) 사용하여 모든 경우 계산

  ```python
  from itertools import combinations
  for new_lst in combinations(lst, n): #lst의 원소 중 n개 뽑아 사용
      pass
  ```

- 1952 [모의 SW 역량테스트] 수영장 : 달을 노드삼아 DFS 돌리면 끝

## 0302

- 4008[모의 SW 역량테스트] 숫자 만들기 : 조건 <숫자 순서 고정, 연산자 우선 순위X> >>> 연산자사용DFS

- 5658  [모의 SW 역량테스트] 보물상자 비밀번호 : 스트링>16진수계산, sorted 구현 해보기

  ```python
  res.add(int(n[i:i+wl],16)) #n:16진수 스트링형태 저장, wl:자릿수, add:set에 추가
  ```

  

재귀함수 : 내부 동작은 동일 >>> 하나의 함수를 반복 사용

```python
#부분집합의 합 >>> 모든 경우의 수 고려
def f(n, k): #호출단계n, 최종단계k
    if n == k: 
        s = 0
    	for i in range(k):
            if b[i] == 1:
                s += A[i]
        return s
    else:
        b[n] = 0
        f(n+1, k)
        b[n] = 1
        f(n+1, k)
       
```

```python
#부분집합의 합2 >>> 모든 경우의 수 고려
def f(n, k, s):
    if n == k: 
        return s
    else:
        f(n+1, k, s+A[n])
        f(n+1, k, s)
```

```python
#부분집합의 합3 >>> 원소 cnt개 만큼 고르는 경우
def f(n, k, cnt, s):
    global res
    if cnt == 0:
        res.append(s)
        return
    elif n == k: 
        return
    else:
        f(n+1, k, cnt-1, s+A[n])
        f(n+1, k, cnt, s)
```

```python
#서로 다른 k개의 자연수 집합에서 부분집합의 원소의 합이 m인 경우의 수
def f(n, k, s, m):
    global cnt
    global A # 배열은 global 선언 안 해도 되긴 함, or A도 인자로 넣어주면 좋음
    if s == m: # 남은 원소 고려 불필요
        cnt += 1
        return
    elif n == k: # 남은 원소 0
        return
    else:
        f(n+1, k, s+A[n], m) # 부분집합에 A[n] 포함
        f(n+1, k, s, m)		 # 부분집합에 A[n] 미포함
```

# 0303

- 1861 정사각형방 : <1~N²까지 중복되지 않은 숫자> : 각 수열은 1씩 증가하며 유니크 하다!!! 

  기준점+1찾기 : visited활용 > 이미 찾은 수열보다 작은 수열 거름

  기준점±1찾기 : visited활용 > 각 수열의 완전한 버전을 한 번에 찾음

  1~N² 배열 활용 : 숫자 주변 +1 True > 가장 긴 배열길이+1

- 1953 [모의 SW 역량테스트] 탈주범 검거 : 4방향 서치시 연결 여부 고민!

  DFS : visited = F > 이동한거리로 저장, 더 짧은 이동거리로 만나면 w에 추가 가능!

  BFS : visited & not in s 활용 > DFS보다 해당 문제에 적절 

# 0304

- 1865 동철이의 일 분배 : 각 선택 (DFS), 백트래킹필수
- 4012 [모의 SW 역량테스트] 요리사 : 음식 반 가르기(DFS)

순열 만들기

```python
def f(n, k):
    if n == K:
        print(p)
    else:
        for i in range(k):
            if not usued[i]: #자리를 바꾸는 코드도 존재
                used[i] = True
                p[n] = a[i]
                f(n+1, k)
                used[i] = False
```

조합 만들기

```python
def f(n, k, s, N):
    if n == K:
        print(C)
    else:
        for i in range(s, N-k+n+1):
            C[n] = i
            f(n+1, k, i+1, N)
N = 10
k = 3
C = [0]*k
f(0, k, 0, N) # C[0], C의 크기 3, 구간 시작 0, 총 후보 10
```

```python
def taste(food, k):
    s = 0
    for i in range(k//2):
        for j in range(i+1, k//2):
            s += synergy[food[i]][food[j]]
            s += synergy[food[j]][food[i]]
    return s
```

# 0305

- 2819 격자판의숫자이어붙이기 : DFS, 중복 : set과 add활용

  - 원하는 수열 찾기
  
  ```python
  a = [1,2,3,4,5] #찾고자 하는 수열
  di, dj = 알맞게
  v = [ [False]*W for _ in range(H)]
  for i in range(W):
      for j in range(H):
          if board[i][j] == a[0]:
              v[i][j] = True
              f(0, 6, i, j)# n == 6 엔딩
              v[i][j] = False
  def f(n, k, i, j):
  	if n == k:
          return True
      for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
          ni, nj = i+di, j+dj
          if 0<=ni<=W-1 and 0<=nj<=H-1 and a[n+1]==board[ni][nj] and not v[ni][nj]:
              v[ni][nj] = True
              if f(n+1, k, ni, nj):
                  return True
              v[ni][nj] = False
    return False
  ```

- 5656 벽돌깨기 : 중복사용가능, 시뮬레이션

  - 1~M까지 숫자로  K자리 수열 만들기 (중복사용가능)

  ```python
  def f(n, K, intv):
      if n == K:
          res.add(intv)
      else:
          for i in range(1, M+1):
              f(n+1, K, intv*10+i)
  res = set()
  f(0, K, intv)
  ```

  

# 0306

- 3752 가능한 시험 점수 : 이전단계까지 누적 리스트 + 이번 점수 합 누계 (비트연산시  `|=` )

  - 아이디어 1 : 부분집합의 합 >>> 중복제거 >>> but... 부분집합 2^100

  - 아이디어 2 : 점수 누적 >>> 중복 제거

  - ```python
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        p = list(map(int, input().split())) #문제별 점수
        ans = [0] #0점인 경우
        
        for x in p:
            num = []
            for y in ans:
                num.append(x+y)
            ans += num
        print('#{tc} {len(set(ans))}')
    ```

  - 아이디어 3 : 중복 제거를 set으로 >>> 큰 리스트 형성 막음

  - ```python
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        p = list(map(int, input().split())) #문제별 점수
        ans = set([0]) #0점인 경우
        
        for x in p:
            num = set()
            for y in ans:
                num.add(x+y)
            ans = set(list(ans)+list(num))
        print('#{tc} {len(set(ans))}')
    ```

  - 아이디어 4 : 0~만점 인덱스 배열, 초기 : 0점 True , A[i] = True 이면 A[i+k] = True

    방금 전 만들어진 숫자 잘 못 사용하지 않도록 조심

  - ```python
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        p = list(map(int, input().split())) #문제별 점수
        total = sum(p)
        s = [0]*(total+1)
        s[0] = 1
        for x in p: # x점 문제에 대해
            for i in range(total-x, -1, -1):
                if s[i] == 1: #i점이 가능하면
                    s[i+x] = 1 #i+x점도 가능
        print('#{tc} {sum(s)}')
    ```

  - ```python
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        p = list(map(int, input().split())) #문제별 점수
        total = sum(p)
        s = [0]*(total+1)
        s[0] = 1
        for x in p:
            for i in range(total-x, -1, -1):
                s[i+x] = s[i+x]|s[i] #i점이 가능하면 i+x점도 가능, 비트연산
        print('#{tc} {sum(s)}') 
    ```

  - 아이디어 5 : 오른쪽부터 탐색. A[i - k] = True 이면 A[i] = True

  - 아이디어 6 : 아이디어 2+4

    A[리스트각원소+k] = F 이면 A[리스트각원소+k] = T  그리고 리스트.append(k)

- 1949 [모의 SW 역량테스트] 등산로 조성 : NxN*K 최대값 320 >>> 선 공사, DFS 시뮬, v 불필요 (∵감소해야만하는 수열)

  - 고유번호와 좌표

  ```python
  K = i*W + j
  i, j = K//W, K%W
  ```

  - DFS

  ```python
  def DFS(r, c, possible, cnt):
      global res
      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          nr, nc = r+dr, c+dc
          if 0 <= nr <= N-1 and 0 <= nc <= N-1:
              if d[r][c] > d[nr][nc]:
                  v[nr][nc] = True #이미 지나온 등산로 보호
                  DFS(nr, nc, possible, cnt+1)
                  v[nr][nc] = False
              elif possible and not v[nr][nc] and d[r][c] > d[nr][nc] - K:
                  temp, d[nr][nc] = d[nr][nc], d[r][c]-1
                  DFS(nr, nc, 0, cnt+1)
                  d[nr][nc] = temp
  ```

  