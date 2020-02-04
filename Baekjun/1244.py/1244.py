# 1~ N 자연수
# 남학생 : 배수 상태 변화
# 여학생 : 대칭 상태 변화
'''
--입력--
N 스위치 개수
정수 스플릿 스위치 상태
S 학생수
성별(남1,여2) 정수(1~N)
---------------------데이터
N = 정수
S = 정수
switch = [0~N]
s[0],s[1]
----------------------
학생
S 반복
if s[0] == 1:
    for i in len(switch):
        if not((i + 1) // s[1]):
            switch[i] = 1 if switch[i] == 0 else 0
else:
    idx s[1]
    while true:

'''
#import sys
#sys.stdin = open("input.txt")
"""
N = int(input())
switch = list(map(int, input().split()))

S = int(input())

for _ in range(S):
    

    s = list(map(int, input().split()))

    if s[0] == 1:
        idx = s[1] # 3 6 9 12
        while (idx <= N): #1~N
            switch[idx-1] = 1 if switch[idx-1] == 0 else 0 # 3-1...
            idx += s[1]
    
    else:
        idx = s[1]-1
        i = 1

        switch[idx] = 1 if switch[idx] == 0 else 0
        while True:
            if 0 > idx-i or idx+i > N-1:
                    break            
            if switch[idx-i] ==  switch[idx+i]:
                switch[idx-i] = 1 if switch[idx-i] == 0 else 0
                switch[idx+i] = 1 if switch[idx+i] == 0 else 0
                i += 1

            else:
                break
for i, v in enumerate(switch):
    if i and (i) % 20 == 0:
        print()
    print(v, end=' ')
"""

#-----재구꺼-------------------
import sys
sys.stdin = open('input.txt')
'''
n : 스위치 수
data : 스위치 상태
s : 학생 수
sex : 성별
num : 받은 숫자
'''
n = int(input())
data = list(map(int, input().split()))
s = int(input())
for _ in range(s):
    sex, num = map(int, input().split())
    # 남자일 때
    if sex == 1:
        a = 1
        while a <= len(data)//num :
            if data[a*num-1] == 1:
                data[a*num-1] = 0
            else :
                data[a*num-1] = 1
            a += 1
    # 여자일 때
    else:
        # data[num-1] 기준점
        left = len(data[:num-1])
        right = len(data[num:])
        length = min(left, right)
        a = 1
        while a <= length :
            if data[num-1-a] == data[num-1+a] :
                if data[num-1-a] == 1:
                    data[num-1-a] = 0
                    data[num-1+a] = 0
                else:
                    data[num-1-a] = 1
                    data[num-1+a] = 1
            else:
                if data[num-1] == 1:
                    data[num-1] = 0
                else:
                    data[num-1] = 1
            a += 1
        if data[num-1] == 1:
            data[num-1] = 0
        else:
            data[num-1] = 1
for i in data:
    print(i, end=' ')