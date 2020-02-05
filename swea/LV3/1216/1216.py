#Thank to hs
def go(s):
    n = len(s)
    mid = n//2
    for i in range(mid):
        if s[i]!=s[n-1-i]:
            return False
    return True
 
for _ in range(1, 10+1):
    test = int(input())
    print('#{}'.format(test), end=' ')
     
    a = []
    for _ in range(100):
        a.append(list(input())) # 데이타셋만들기 str형식
    res = 0
    for cnt in range(100, 0, -1):#cnt 99부터 계산~1
        flag = False
         
        for i in range(100): #행0~99
            for j in range(101-cnt): # 0~(1~99)
                tmp = ''.join(a[i][j:j+cnt]) #[0:99] !
                if go(tmp):
                    flag=True
                    break
        if flag:
            res = cnt
            break
        for j in range(100):
            for i in range(101-cnt):
                tmp = ''
                for k in range(i, i+cnt):
                    tmp += a[k][j]
                if go(tmp):
                    flag=True
                    break
        if flag:
            res = cnt
            break
    print(res)