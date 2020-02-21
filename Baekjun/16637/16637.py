import sys
sys.stdin = open('input2.txt')
'''
N : 1~19, 최대 숫자 10, 연산자 9로 제한 되어있는것 확인
------------------------------------------------------------
괄호
의미 : 해당 연산을 먼저 시행한다 (나머진 우선순위 없는 순차 연산)
중복 괄호 불가 : 두번째 연산자에 괄호 씌웠다 == 양 옆의 첫번째 두번째 연산자 괄호 불가
--------------------------------------------------------------------------------
가능한 모든 경우의 수 연산 하였음
가능한 경우 뽑기 : 연산자로 만들 수 있는 모든 부분집합 생성 >>> 중복 괄호 불가 특성 적용하여 추출
-----------------------------------------------------------------------------------------
res = -99999 초기화 : 0으로 초기화시 음수 결과값에 대한 커버
'''
def calc(a, b, c):
    if c == '+':
        return a+b
    if c == '-':
        return a-b
    if c == '*':
        return a*b

def getSubset(lst):
    n = len(lst)
    s = []
    for i in range(1<<n):
        flag = False
        temp = []
        for j in range(n):
            t_f = i & (1 << j)
            if t_f: # t_f 가 0 이 아닌 경우에는 출력.
                temp.append(lst[j])
        else:
            s.append(temp)
    return s

def my_get(lst):
    for i in range(len(lst)-1, 0, -1):
        flag = False
        for c1 in lst[i][:-1]:
            for c2 in lst[i][1:]:
                if abs(c1-c2) == 1:
                    lst.pop(i)
                    flag = True
                    break
            if flag:
                break
    return lst
    
def calc_str(nums, ops):
    temp = nums[0]
    for i in range(len(ops)):
        temp = calc(temp, nums[i+1], ops[i])
    return temp

def go(nums, ops, n_idxs):
    res = -999999
    for idxs in n_idxs:
        temp1 = nums[:]
        temp2 = ops[:]
        for idx in idxs[::-1]:
            temp = calc(temp1.pop(idx), temp1.pop(idx), temp2.pop(idx))
            temp1.insert(idx, temp)
        ret = calc_str(temp1, temp2)
        res = ret if ret > res else res
    return res

T = 1 #테스트케이스 수만큼 돌려보고 싶으면 조절
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    d = sys.stdin.readline()
    nums, ops = [], []
    for i in range(N):
        if i % 2 :
            ops.append(d[i])
        else:
            nums.append(int(d[i]))
    n_idxs = (my_get(getSubset(list(range(len(ops))))))
    print(go(nums, ops, n_idxs))



