def go2(field, x, y): #메인 함수
    if x == x2 and y == y2:
        return 1
    #좌/우/상/하
    dx = [ 0, 0,-1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4): #4방향 서치
        if 0<=x+dx[k]<=15 and 0<=y+dy[k]<=15: #경계조건
            if field[x+dx[k]][y+dy[k]] == 3: #길이면
                return 1
            elif field[x+dx[k]][y+dy[k]] == 0:
                field[x+dx[k]][y+dy[k]] = 1 #길을 잠시 닫음
                if go(field, x+dx[k], y+dy[k]): #go
                    return 1
                field[x+dx[k]][y+dy[k]] = 0 #길을 다시 복구

            elif field[x+dx[k]][y+dy[k]] == 3: #종료도착 >>> 출력 res[0] = 1
                res[0] = 1
                return