# SW Expert Academy

## Level 2

### numbers = list(map(int,input().split(' ')))
> 입력을 정수 리스트로 변환하기
```python
numbers = list(map(int,input().split(' ')))
P, Q, R, S, W= numbers
```

### 리스트 내포?
> 입력된 정수의 각 자리수를 이용하는 문제
#### 1. Num_List = [int(x) for x in str_num] 
> 숫자>스트링>각자리접근>리스트저장
#### 2. 타겟 = list ( filter ( lambda x :x not in Num_List , 타겟) )
> 타겟 필터링하기

### max(리스트); 리스트.index(값); 리스트=리스트[max_index+1 : ]
> 백만장자 : max값의 인덱스를 이용한 계산으로 복잡도 줄이기

### int_ascii = ord(스트링); sts = chr(int_ascii)
> 문자열 ↔ 아스키코드 변환
> 스트링 간 비교 가능

### dict[idx] =value 
> dict항목 추가

### .append()
> 리스트안에 리스트를 만들어 N중 배열을 만드는데 활용
- 방법1 data_list = list(); data_list.append(리스트)
- 방법2 temp= list(); temp.append(값); data_list.append(temp) 

### input().strip()
> 여러 개 값을 input 받을때, input값에 공백이 있어 문제가 생기는것 방지

### 1204.[S/W 문제해결 기본] 1일차 - 최빈수 구하기

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
T = int(input())

for T in range(T):
    n = int(input())
    numbers=list(map(int,input().strip().split(' ')))
    cases = sorted(list(set(numbers)))
   # print(cases)
    max_cnt = 0
    max_num = 0
    for case in cases:
        temp_cnt = 0
        for number in numbers:
            if number == case:
                temp_cnt +=1
        if temp_cnt >= max_cnt :
            max_cnt = temp_cnt
            max_num = case
    print('#{} {}'.format(n, max_num))
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



### 1859.백만 장자 프로젝트

25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
각 날의 매매가는 10,000이하이다.
[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.
[예제 풀이]
1번째 케이스는 아무 것도 사지 않는 것이 최대 이익이다.
2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익을 얻을 수 있다.

```python
T=int(input())

for t in range(T):
    N=int(input())
    data_input=list(map(int,input().split(' ')))
    #print(data_input)
    result = 0
    start_index, max_value , max_index, temp =0, 0, 0, 0
    while True :
        #print('s_index : {}, max_v : {}, max_i : {}, temp : {}'.format(start_index, max_value , max_index, temp))
        temp = 0
        max_value = max(data_input) #값
        max_index = data_input.index(max_value)					#인덱스
        if max_index != 0:
            temp = max_index * max_value
            for i in range(max_index):
                temp -= data_input[i]
            result += temp
            #print('result={}, temp={}'.format(result, temp))
        if max_index == len(data_input)-1 or max_index == len(data_input) -2 :
            #print('break')
            break
           
        else:
            #print('continue')
            data_input = data_input [max_index+1 : ]
            #print(data_input)
        

    print ('#{} {}'.format(t+1, result))
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
#print (0b01001100)
#print (chr(76))

#print('A:{},Z:{},a:{},z:{},0:{},1:{},9:{},+:{},/:{}'.format(ord('A'),ord('Z'),ord('a'),ord('z'),ord('0'),ord('1'),ord('9'),ord('+'),ord('/')))
#A:65,Z:90,a:97,z:122,0:48,9:57,+:43,/:47
#A~Z : -65 a~z : -71 0~9 : +4 : # : +19 / : +16

T= int(input())
for T in range(T):
    sts = input()
    
    print('#{} '.format(T+1),end='')
    st = [0,0,0,0]
    i=0
    for idx, val in enumerate(sts):
        #print(val,end='')
        if 'A' <= val <= 'Z':
            st[idx%4] = ord(val) - 65
        elif 'a' <= val <= 'z':
            st[idx%4] = ord(val) - 71
        elif '0' <= val <= '9':
            st[idx%4] = ord(val) + 4
        elif '+' == val:
            st[idx%4] = ord(val) + 19
        elif '/' == val:
            st[idx%4] = ord(val) + 16
        if idx % 4 == 3:
#24개받기 = 문자열4개 받기 st1 st2 st3 st4
#문자 1: st1*4 + (st2//16)
#문자 2: (st2%16)*16 + (st3//4)
#문자 3: (st3%4)*64 + st4
            st0 ,st1, st2 = '' , '' , ''
            st0 = st[0]*4 + (st[1]//16)
            st1 = (st[1]%16)*16 + (st[2]//4)
            st2 = (st[2]%4)*64 + st[3]
            #print (' : ', end='')
            print (chr(st0),end='')
            print (chr(st1),end='')
            print (chr(st2),end='')
            #print ('')

    print('')
    
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

### 1945.간단한 소인수분해

숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.
[제약 사항]
N은 2 이상 10,000,000 이하이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
"""
T = int(input())
divs = [2, 3, 5, 7, 11]
result =[0, 0, 0, 0, 0]
for t in range(T):
    number=int(input())
    i=0
    for div in divs:
        temp = 0
        while number%div==0:
            number = number//div
            temp +=1
        result[i] = temp
        i +=1
    print('#{0} {1} {2} {3} {4} {5}'.format(t+1, result[0], result[1], result[2], result[3], result[4]))
"""

T = int(input())
divs = [2, 3, 5, 7, 11]
result =dict()
for t in range(T):
    number=int(input())
    i=0
    for div in divs:
        temp = 0
        while number%div==0:
            number = number//div
            temp +=1
        result[div] = temp
        i +=1
    print('#{0} {1} {2} {3} {4} {5}'.format(t+1, result[2], result[3], result[5], result[7], result[11]))
```



### 1946.간단한 압축 풀기

원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.
[예제]
압축된 문서의 내용
A 10
B 7
C 5
압축을 풀었을 때 원본 문서의 내용
AAAAAAAAAA
BBBBBBBCCC
CC
[제약사항]

1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)
2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)
3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)
4. 원본 문서의 너비는 10으로 고정이다.
   [입력]
   가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
   각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.
   [출력]
   각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
   (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T = int(input())

for t in range(T):
    N = int(input())
    temp = ""
    length = 0
    for n in range(N):
        x , y = list(input().split(' '))
        y = int(y)
        temp+= x * y
        length += y
 #   length = len(temp)
    i=0
    print('#{}'.format(t+1))
    for word in temp:
        print(word,end='')
        i+=1
        if i == 10 :
            print('')
            i=0
    print('')
```

### 1948.날짜 계산기

월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.
[제약 사항]
월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T = int(input())
dates ={
    1 : 31,    2 : 28,    3 : 31,    4 : 30,    5 : 31,    6 : 30,    7 : 31,
    8 : 31,    9 : 30,    10 : 31,    11 : 30,    12 : 31,
}
for t in range(T):
    result=0
    data_input = list(map(int,input().split(' ')))
    for i in range( data_input[0] , data_input[2] ):
        result += dates[i]
    result += data_input[3] - data_input[1] +1
    print('#{} {}'.format(t+1, result))
```

### 1954.달팽이 숫자

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
[제약사항]
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T = int(input())

for t in range(T):
    N = int(input())
    dicts = {
        0:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        1:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        2:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        3:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        4:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        5:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        6:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        7:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        8:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
        9:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
    }
    n = 1
    r, c =0, -1
    plus_r = [ 0, 1, 0, -1 ]
    plus_c = [ 1, 0, -1, 0 ]
    #k=0
    for i in range ( 1 , 2*N ):
        for _ in range ( N - (i//2) ):
            r += plus_r[(i-1)%4]
            c += plus_c[(i-1)%4]
            dicts[r][c] = n
            #print(dicts)
            n += 1        
        #k+=1
    print('#{}'.format(t+1))
    for a in range(N):
        for b in range(N):
            print ('{}'.format(dicts[a][b]), end=' ')
        print('')
```





### 1959.두 개의 숫자열

N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
위 예제의 정답은 아래와 같이 30 이 된다.
[제약 사항]
N 과 M은 3 이상 20 이하이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
두 번째 줄에는 Ai,
세 번째 줄에는 Bj 가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T=int(input())
for t in range(T):
    N, M = list(map(int, input().split(' ')))
    N_num = list(map(int, input().split(' ')))
    M_num = list(map(int, input().split(' ')))
    if N >= M :
        N, M = M, N
        N_num, M_num = M_num, N_num
    #N작고 M이 큰 상태
    result=0
    for i in range( M-N+1 ):
        temp=0
        for k in range(N):
            temp += N_num[k] * M_num [k+i]
        if temp >= result :
            result = temp
    print('#{} {}'.format(t+1,result))
```

### 1974.스도쿠 검증

9x9 스도쿠
검증 O : 1 , 검증 X : 0
[제약 사항]
1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T = int(input())
for T in range(T):
    data = list()
    for _ in range(9):
        data.append(list(map(int, input().strip().split(' '))))
 #   print (data)
    
    result = 1 #초기값
    #row 검증
    for idx, numbers in enumerate(data):
        for num in range (1,10):
            if not ( num in numbers) :
                #print('row 걸림, idx : {} num : {}'.format(idx, num))
                result = 0
   
    #col 검증
    for x in range(9):
        temp = list()
        for y in range(9):
            temp.append(data[y][x])
            
        for num in range(1,10):
            if not ( num in temp):
                #print('col 걸림, x : {}, y : {}, num : {}'.format(x, y, num))
                result = 0
    
    for x in range(0,9,3):
        temp = list()
        for y in range(0,9,3):
            for xi in range(3):
                for yi in range(3):
                    temp.append(data[y+yi][x+xi])
            for num in range(1,10):
                if not ( num in temp):
                    #print('box 걸림, x : {}, y : {}, num : {}'.format(x, y, num))
                    result = 0
    print('#{} {}'.format(T+1,result))
```


```python
T = int(input())
for T in range(T):
    result = 1
    data_list = list()
    for _ in range(9):
        data_list.append(list())
    
    for i in range(3):
        for _ in range(3):

            temp = list(map(int, input().split(' ')))
            data_list[i*3+0] += temp[0:3]
            data_list[i*3+1] += temp[3:6]
            data_list[i*3+2] += temp[6:9]
    for d in data_list:
        print(d)
            


"""
T = int(input())
for T in range(T):
    data_list = list()
    for _ in ranger(9):
        data_list.append(list())
	print(data_list)    
    result=0
    
    for i in range(0,9):
        temp = list(map(int, input().split(' ')))
        data_list[(i   )%3].append(temp[0:2])
        data_list[(i+1)%3].append(temp[0:2])
        data_list[(i+2)%3].append(temp[0:2])
        if len(temp) != len(list(set(temp))) :
            result = 2
    print(data_list)

    if result == 2:
        print('#{} {}'.format(T+1, result-2))
        break
    else:
        for _ in range(9):
            tempssss = 0
            for _ in range(3):
                for _ in range(3):
                    if 
"""
```


### 1983.조교의 성적 매기기

학기가 끝나고, 학생들의 점수로 학점을 계산중이다.
학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.
학점은 학생들이 응시한 중간35 /기말고사45 과제20 반영
10 개의 평점을 총점이 높은 순서대로 부여하는데,
각각의 평점은 같은 비율로 부여할 수 있다.
예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
[제약사항]

1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.
   [입력]
   입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
   다음 줄부터 각 테스트 케이스가 주어진다.
   테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
   테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
   [출력]
   테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
   (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
val = [ 'A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0' ]
T=int(input())
for T in range(T):
    grades = list()
    N, K = list(map(int, input().split(' '))) #N 총학생수, K알고싶은 학생순서
    order=N
    n = N//10
    for N in range(N):
        score = 0
        scores = list(map(int, input().split(' '))) #3개의 데이터가 저장
        #7 9 4
        score = scores[0]*7+scores[1]*9+scores[2]*4
        grades.append(score) # index 0부터 score 들어감
   # print('오더는 : {}'.format(order))
    for grade in grades:
        if grades[K-1] > grade :
            order-=1
           # print(order)
    for i in range(0,10):
        if order <= (i+1)*n :
            print('#{} {}'.format(T+1, val[i]))
            break
```


### 1926.간단한 369게임

3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.
1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
  1 2 3 4 5 6 7 8 9…
2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
[제약사항]
N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N 이 주어진다.
[출력]
1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.

```python
N = int(input())

for N in range(1,N+1):
    result=0
    num_list = [int(N) for N in str(N)]
    #print(num_list)
    for num in num_list:
        if num % 3 == 0 and num != 0 :
            result+=1
    if result == 0 :
        print(N, end=' ')
    else:
        print('-'*result,end=' ')
print('')
```


### 1961.숫자 배열 회전 

```python
T = int(input().strip())
for T in range(T):
    N = int(input().strip())
    
    data_0 = list()
    for _ in range(N):
        data_0.append( list(map(int, input().strip().split(' '))) )
    data_90 = list()
    
    for y in range(N):
        temp = list()
        for x in range(N):
            #data_90[ x ][ x + (-x-y+N-1) ] = data_0[y][x]
            #print('y,x : {},{}'.format(y,x))
            temp.append(data_0[-x+(N-1)][y])
        data_90.append(temp)

    data_180 = list()
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data_90[-x+(N-1)][y])
        data_180.append(temp)

    data_270 = list()
    for y in range(N):
        temp = list()
        for x in range(N):
            temp.append(data_180[-x+(N-1)][y])
        data_270.append(temp)
    print('#{}'.format(T+1))
    for a in range(N):
        for b in range(N):
            print('{}'.format(data_90[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_180[a][b]),end='')
        print('',end=' ')
        for b in range(N):
            print('{}'.format(data_270[a][b]),end='')
        print('')
```

### 1966.숫자를 정렬하자
```python
T = int(input())
for T in range(T):
    length = int(input())
    numbers = sorted(list(map(int, input().split(' '))))
    print('#{}'.format(T+1),end=' ')
    for number in numbers:
        print(number,end=' ')
    print('')
    
""" 중복값을 처리하지 못해 아래 거는 사용 못함 ㅠㅠ 
    length = int(input())
    numbers = list(map(int, input().split(' ')))
    idxs = list()
    
    for number in numbers:
        temp = 0
        for i in range(length):
            if numbers[i] < number :
                temp +=1 #temp 0~N-1 순위
        
        idxs.append(temp)
    temp = list(range(length))
    for i, idx in enumerate(idxs):
        temp[idx] = i
    print('#{}'.format(T+1),end=' ')
    for n in temp:
        print(numbers[n],end=' ')
    print('')
"""
```

### 1970.쉬운 거스름돈

```python
#coins = [ 50000, 10000, 5000, 1000, 500, 100, 50, 10 ]
dict_coins ={
    50000 : 0,
    10000 : 0,
    5000 : 0,
    1000 : 0,
    500 : 0,
    100 : 0,
    50 : 0,
    10 : 0,
}
T = int(input())

for T in range(T):
    cost = int(input())
    for key, val in dict_coins.items():
        dict_coins[key] = cost // key
        cost = cost % key
        #if cost == 1 :
            #dict_coins[10] = 1
    print('#{}'.format(T+1))
    for key in dict_coins:
        print (dict_coins[key],end=' ')
    print('')
```

### 1976.시각 덧셈

```python
T = int(input())
for T in range(T):
    y1, m1, y2, m2 = list(map(int, input().strip().split(' ')))
    m = (m1+m2)%60
    y = (y1 + y2 + (m1+m2)//60)%13 + (y1 + y2 + (m1+m2)//60)//13
    print ('#{} {} {}'.format(T+1, y, m))
```

### 1979.어디에 단어가 들어갈 수 있을까

```python
T = int(input())
for T in range(T):
    N, K = list(map(int, input().split(' ')))
    
    result = 0
    data = list()
    for _ in range(N):
        temps = list(map(int, input().strip().split(' ')))
        data.append(temps)
    
    for i in range(N):
        cnt = 0
        for k in range(N):
            if data[k][i] == 1:
                cnt +=1
                if cnt == K and k == N-1:
                    result += 1
            else :
                if cnt == K :
                    result += 1
                cnt = 0
    
    for i in range(N):
        cnt = 0
        for k in range(N):
            if data[i][k] == 1:
                cnt +=1
                if cnt == K and k == N-1:
                    result += 1
            else :
                if cnt == K :
                    result += 1
                cnt = 0
    print('#{} {}'.format(T+1, result))
                    
```

### 1984.중간 평균값 구하기

10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T=int(input())
for T in range(T):
    data_input = list(map(int,input().strip().split(' ')))
    result = round( (sum(data_input) - max(data_input) - min(data_input) ) / 8 )
    print('#{} {}'.format(T+1,result))   
"""두번째 버전
T=int(input())
for T in range(T):
    data_input = list(map(int,input().strip().split(' ')))
    sum_num, max_num, min_num = 0, 0, 10000
    for data in data_input:
        if data > max_num:
            max_num = data
        if data < min_num :
            min_num = data
        sum_num += data
    result = round( (sum_num - max_num - min_num) / 8 )
    print('#{} {}'.format(T+1, result ))
"""
```

### 1986.지그재그 숫자 

```python
T = int(input())
for T in range(T):
    N = int(input())
    result = 0
    for i in range (1,N+1,2):
        result += i
    for k in range (2,N+1,2):
        result -= k
    print('#{} {}'.format(T+1, result))
```

### 1989.초심자의 회문 검사

회문이면 1, 아니면 0을 출력
[제약 사항]
각 단어의 길이는 3 이상 10 이하이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
T= int(input())
for T in range(T):
    result=1
    words = input() #string
    
    for i in range( len(words) // 2) :
        if words[i] != words[-i-1]:
            result=0
            break
    print('#{} {}'.format(T+1, result))
```


### 2001.파리 퇴치

```python
T = int(input())
for T in range(T):
    N, M = list(map(int, input().strip().split(' ')))
    
    data = list()
    for _ in range(N):
        data.append( list(map(int, input().strip().split(' '))) )
        
    #0~N-M
    result = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            temp = 0
            for yi in range(M):
                for xi in range(M):
                    temp += data[y+yi][x+xi]
            if temp > result:
                result = temp
    print('#{} {}'.format(T+1, result))
```

### 2005.파스칼의 삼각형

#### list1.append(int값) 으로 리스트 만든후 list2.append(list1) 으로 이중배열 완성
```python
T = int(input())
for T in range(T):
    N = int(input())
    
    data = list()
    for k in range(N):
        temp = list()
        for i in range(k+1):
            if i == 0 or i == k:
                temp.append(1)
            else:
                temp.append ( data[k-1][i-1]+data[k-1][i] )
        data.append(temp)
    print('#{}'.format(T+1))
    for k in data:
        for i in k:
            print(i, end=' ')
        print('')
                
```

### 2007.패턴 마디의 길이
```python
T = int(input().strip())
for T in range(T):
    words = input().strip()
    
    index = list()
    n = len(index) #6
    for idx, word in enumerate(words):
        if word == words[0] : 
            index.append(idx)
    length = list()
    for i in range( len(index )-1):
        length.append( index[i+1] - index[i] )
    length.append( 30 - index [len(length)] )
   # print(index)
  #  print(length)
    
    cases = [n for n in index if 0< n<= 10 ] 
    #print (cases)
    result = 0
    for case in cases:
        i=0
        if result != 0:
            if case % result == 0:
                break
        for word in words[0:case]:
            if word != words[case+i]:
                break
            else:
                i += 1
                if i == case:
                    result = case
    print('#{} {}'.format(T+1,result))
```