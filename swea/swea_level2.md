# SW Expert Academy

## Level 2

1859.백만 장자 프로젝트
1926.간단한 369게임
2007.패턴 마디의 길이
2005.파스칼의 삼각형
2001.파리 퇴치
1989.초심자의 회문 검사
1986.지그재그 숫자
1984.중간 평균값 구하기
1983.조교의 성적 매기기
1979.어디에 단어가 들어갈 수 있을까
1976.시각 덧셈
1974.스도쿠 검증
1970.쉬운 거스름돈
1966.숫자를 정렬하자 
1961.숫자 배열 회전 
1959.두 개의 숫자열
1954.달팽이 숫자 
1948.날짜 계산기
1946.간단한 압축 풀기
1945.간단한 소인수분해
1940.가랏! RC카! 
1928.Base64 Decoder
1288.새로운 불면증 치료법 
1285.아름이의 돌 던지기
1284.수도 요금 경쟁
1204.[S/W 문제해결 기본] 1일차 - 최빈수 구하기

### 1204.[S/W 문제해결 기본] 1일차 - 최빈수 구하기 - 미해결



어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
다음과 같은 수 분포가 있으면,
10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
최빈수는 8이 된다.
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
[제약 사항]
학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

```python
import collections
T = int(input())

for i in range(T):
    n = int(input())
    numbers=list(map(int,input().split(' ')))
    dict_cnt = dict(collections.Counter(numbers))
    max_cnt = max(dict_cnt.values())
    temp=0
    for k in dict_cnt.keys():
        print(k)
        if dict_cnt[k] == max_cnt:
            temp = k
    else:
        print('#{} {}'.format(n,temp))
```


### 1284.수도 요금 경쟁
삼성전자에 입사한 종민이는 회사 근처로 이사를 하게 되었다.
그런데 집의 위치가 두 수도 회사 A, B 중간에 위치하기에 원하는 수도 회사를 선택할 수 있게 되었는데, 두 회사 중 더 적게 수도 요금을 부ㅍ담해도 되는 회사를 고르려고 한다.
종민이가 알아본 결과 두 회사의 수도 요금은 한 달 동안 사용한 수도의 양에 따라 다음과 같이 정해진다.
A사 : 1리터당 P원의 돈을 내야 한다.
B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.
[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 종민이가 내야 하는 수도 요금을 출력한다.

#### 입력을 정수 리스트로 변환하기 : numbers = list(map(int,input().split(' ')))

```python
T = int(input())
#P, Q, R, S, W
#PW
#Q + (W-S
for i in range(T):
    numbers = list(map(int,input().split(' ')))
    P, Q, R, S, W= numbers
    pay_A = P*W
    temp = W-R
    if temp<=0 :
        temp=0
    pay_B = Q +(temp)*S
    if pay_A >= pay_B :
        print('#{} {}'.format(i+1, pay_B))
    else:
        print('#{} {}'.format(i+1, pay_A))
```

### 1285.아름이의 돌 던지기 C++만 제출
아름이를 포함하여 총 N명의 사람이 돌 던지기 게임을 하고 있다.
이 돌 던지기 게임은 앞으로 돌을 던져 원하는 지점에 최대한 가깝게 돌을 던지는 게임이다.
정확하게 말하면 밀리미터 단위로 -100,000에서 100,000까지의 숫자가 일렬로 써져 있을 때, 사람들은 숫자 100,000이 써져 있는 위치에 서서 최대한 0에 가까운 위치로 돌을 던지려고 한다.
N명의 사람들이 던진 돌이 떨어진 위치를 측정한 자료가 주어질 때, 가장 0에 가깝게 돌이 떨어진 위치와 0 사이의 거리 차이와 몇 명이 그렇게 돌을 던졌는지를 구하는 프로그램을 작성하라.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 돌을 던지는 사람의 수 N(1≤N≤1,000)이 주어진다.
두 번째 줄에는 각 사람이 돌을 던졌을 때 돌이 떨어진 위치를 나타내는 N개의 정수가 공백으로 구분되어 주어진다.
모든 사람이 돌을 그럭저럭 잘 던졌기 때문에, 돌이 떨어지는 위치는 항상   -100,000에서 100,000사이 범위의 정수이다. (-100,000과 100,000도 돌이 떨어질 수 있다.)
[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
돌이 가장 0에 가깝게 떨어진 곳과 0 사이의 거리 차이와 그렇게 던진 사람이 몇 명인지 나타내는 정수를 공백 하나로 구분하여 출력한다.

### 1288.새로운 불면증 치료법 
민석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.
민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.
즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.
이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.
이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
예를 들어 N = 1295이라고 하자.
첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.
현재까지 본 숫자는 0, 1, 2, 5, 9이다.
세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.
현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.
5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 민석이는 양 세기를 멈춘다.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.
[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
( 민석이는 xN번 양을 세고 있다. )

#### 숫자(abcd)를 [a,b,c,d]로 변환 후 : Num_List = [ int(x) for x in str_숫자 ]

#### 타겟 = list ( filter ( lambda x :x not in Num_List , 타겟) )

```python
#테스트코드1~4
T = int(input())		
#T=1                                  #테스트코드1

for i in range(T):
    N=1
    goal = list(range(0,10))
    str_num_origin = input() #초기값, 불변
    #str_num_origin = "1295"                 #테스트코드2

	# print('초기값 : {}'.format(goal)) #테스트코드3
    
    while True:
        int_num = int(str_num_origin) * N #0N 1N 2N ...
        str_num = str(int_num) 		#string : literable로 변환
        num_list = [int(n) for n in str_num]
        goal = list(filter(lambda x :x not in num_list , goal))
        
       # print('#{} : {} , {} '.format(N,goal,int_num))                  #테스트코드4
    
        if goal == []:
            break
        N +=1
    print('#{} {}'.format(i+1,int_num))
"""
#1111
숫자 N
range(N,nN+1,N)

list = list(range(N,n*N+1,N))
ran_list = [str(x) for x in range(N,n*N+1,N)] #각 1N 2N ~ 배열
"""

"""
#222
T = int(input())


for i in range(T):
    N=1
    goal = list(range(0,10))
    str_num = input() #초기값
    int_num = int(str_num) * N #불변
    while goal:
        int_num = int(str_num) * N #0N 1N 2N ...
        str_num = str(int_num) 		#string : literable로 변환
        num_list = [int(n) for n in str_num]
        goal = list(filter(lambda x : x not in num_list , goal))
        if goal == []:
            break
    print('#{} {}'.format(i+1,N))
"""
```

### 1928.Base64 Decoder
다음과 같이 Encoding 을 한다.
    1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
    2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.
입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.
[제약사항]
문자열의 길이는 항상 4의 배수로 주어진다.
그리고 문자열의 길이는 100000을 넘지 않는다.
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```python
# dec = dict()
# for i in range(26):
#     dec[i] = chr(ord(A)+i)
# for i in range(26,52):
#     dec[i] = chr(ord(a)+i)
# for i in range(52.62):
#     dec[i] = str(i)
# dec[62] = '+'
# dec[63] = '/'

T=int(input())
dec = dict() #dec[문자] = int
for i in range(26):
    dec[chr(ord('A')+i)] = i
for i in range(26,52):
    dec[chr(ord('a')+i-26)] = i
for i in range(52,62):
    dec[str(i-52)] = i
dec['+'] = 62
dec['/'] = 63
#print(type(dec))
#print(dec)
for t in range(T):

    data = input() #str
    str_data =''
    cnt= temp0 = temp1 =temp2 =0
    
    for d in data: #str을 순회
        if (cnt%4)==0:
            temp0 += dec[d]*4
        elif (cnt%4) == 1:
            temp0 += dec[d]//16
            temp1 += (dec[d]%16)*16
        elif (cnt%4) == 2:
            temp1 += (dec[d]//4)
            temp2 += (dec[d]%4)*64
        else :
            temp1 += dec[d]
            str_data += chr(temp0) + chr(temp1) + chr(temp2)
            temp0 = temp1 = temp2 = 0
        cnt += 1
    print('#{} {}'.format(t+1,str_data))
```

### 1940. 가랏! RC카!

RC (Radio Control) 카의 이동거리를 계산하려고 한다.
입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.
0 : 현재 속도 유지.
1 : 가속
2 : 감속
위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.
가속도의 단위는, m/s2 이며, 모두 양의 정수로 주어진다.
입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.
RC 카의 초기 속도는 0 m/s 이다.
[예제]
아래 예제 입력에서 정답은 3 이 된다.
입력         시간     RC 카의 속도 RC     카의 이동거리
1 2          1 sec          2 m/s                    2 m
2 1          2 sec          1 m/s                    3 m
[제약사항]
1. N은 2이상 30이하의 정수이다. (2 ≤ N ≤ 30)
2. 가속도의 값은 1 m/s2 혹은 2 m/s2 이다.
3. 현재 속도보다 감속할 속도가 더 클 경우, 속도는 0 m/s 가 된다.
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T, 다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스 첫 줄에는 Command 의 수 N이 주어지고, 둘째 줄부터, 매 줄마다 각각의 Command가 주어진다.
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
#현재속도 , 이동한 거리
#초기화
#커멘드 0/1/2 -> 현재속도변화 , 이동거리 계산

T = int(input())

for i in range(T):
    n = int(input())
    for k in range(n):
        speed = 0
        length = 0
        command = list(map(int,input().spilit()))
        if command[0] == 0 :
            pass
        elif command[0] == 1 :
            speed += command[1]
        else:
            speed -= command[1]
            if speed < 0 :
                speed = 0

        length += speed

print('#{0} {1}'.format(i+1, length))


```