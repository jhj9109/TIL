### 1545. 거꾸로 출력해 보아요
주어진 숫자부터 0까지 순서대로 찍어보세요
```python
num= int(input())
for i in range(num,-1,-1):
    print(i,end=' ')
print('')
```
### 1933.간단한 N 의 약수
입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
[제약사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N 이 주어진다.
[출력]
정수 N 의 모든 약수를 오름차순으로 출력한다.
```python
num=int(input())
for i in range(1,num+1):
    if num%i == 0 :
        print(i,end=' ')
print('')
```

### 1936.1대1 가위바위보
A와 B가 가위바위보를 하였다.
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
[입력]
입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
[출력]
A가 이기면 A, B가 이기면 B를 출력한다.
```python
a, b=list(map(lambda x: int(x),input().split(' ')))
if a==1:
	if b==2:
		print('B')
	else:
		print('A')
elif a==2:
	if b==3:
		print('B')
	else:
		print('A')
else :
	if b==1:
		print('B')
	else:
		print('A')        

```

### 1938. 아주 간단한 계산기
[제약 사항]
1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)
2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.
[입력]
입력으로 두 개의 자연수 a, b가 빈 칸을 두고 주어진다.
[출력]
사칙연산의 결과를 각 줄에 순서대로 출력한다.
```python
a, b = list(map(lambda x: int(x),input().split(' ')))
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
#print(a%b)도 통과
```
### 2019.더블더블
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
```python
num = int(input())
for i in range(0,num+1):
    print(pow(2,i),end=' ')
```


### 2025.N줄덧셈
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
단, 주어질 숫자는 10000을 넘지 않는다.
[예제]
주어진 숫자가 10 일 경우 출력해야 할 정답은,
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

```python
num = int(input())
result=0
for n in range(1,num+1):
    result+=n
print(result)
```

### 2027.대각선 출력하기
주어진 텍스트를 그대로 출력하세요.
```python
print("#++++")
print("+#+++")
print("++#++")
print("+++#+")
print("++++#")
```
### 2029.몫과 나머지 출력하기
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 1이상 10000이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
```python
n = int(input())
for i in range(n):
    num=list(map(lambda x:int(x),input().split(' ')))
    print('#{0} {1} {2}'.format(i+1,num[0]//num[1],num[0]%num[1] ))
```

### 2043.서랍의 비밀번호
서랍의 비밀번호가 생각이 나지 않는다.
비밀번호 P는 000부터 999까지 번호 중의 하나이다.
주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.

[입력]
입력으로 P와 K가 빈 칸을 사이로 주어진다.
[출력]
몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.

```python
num = list(map(lambda x:int(x),input().split(' ')))
n=0
for i in range(num[1],1000):
    n+=1
    if i == num[0]:
        break
print(n)
```
### 2046.스탬프 찍기
주어진 숫자만큼 # 을 출력해보세요.
주어질 숫자는 100,000 이하다.
```python
n = int(input())
print('#'*n)
```
### 2047.신문 헤드라인
신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.
[예제 풀이]
The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.
THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.
[제약 사항]
문자열의 최대 길이는 80 bytes 이다.
[입력]
입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.
[출력]
문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.
```python

data = input()
data_str=''
for d in data:
    if 'a'<=d<='z' :
        data_str+= d.upper() 
    else:
        data_str+= d 
print(data_str)
```



### 2050.알파벳을 숫자로 변환
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
[제약 사항]
문자열의 최대 길이는 200이다.
[입력]
알파벳으로 이루어진 문자열이 주어진다.
[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.

```python
# A=97

data = input()

for d in data:
    print(ord(d)-64,end=' ')
```


### 2056.연월일 달력
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
[그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
n = int(input())
for i in range(n):
	
    #데이터는 str
    data = int(input())
    yy=data//10000
    mm=(data%10000)//100
    dd=data%100
    if not(1<=mm<=12):
        print('#{0} -1'.format(i+1))
    elif  dd>calendar[mm]:
        print('#{0} -1'.format(i+1))
    else :
        print('#{0} {1:04d}/{2:02d}/{3:02d}'.format(i+1,yy,mm,dd))

```
### 2058.자릿수 더하기
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
[제약 사항]
자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
[입력]
입력으로 자연수 N이 주어진다.
[출력]
각 자릿수의 합을 출력한다.
```python
num = input()
result=0
for n in num:
    result += int(n)
print(result)
```

### 2063.중간값 찾기

중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.
[예제]
N이 9 이고, 9개의 점수가 아래와 같이 주어질 경우,
85 72 38 80 69 65 68 96 22
69이 중간값이 된다.
[제약 사항]

1. N은 항상 홀수로 주어진다.
2. N은 9이상 199 이하의 정수이다. (9 ≤ N ≤ 199)
   [입력]
   입력은 첫 줄에 N 이 주어진다.
   둘째 줄에 N 개의 점수가 주어진다.
   [출력]
   N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.

```python
n = int(input())
numbers=list(    map(int,input().split(' '))   ) #len(numbers) = n
#easy
num_list = sorted(numbers)
print(   num_list [  ( (n-1)//2 ) ]   )

```

### 2068.최대수 찾기

10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
#max()버전
n=int(input())
for i in range(n):
    numbers=list(map(int,input().split(' ')))
    print('#{0} {1}'.format( i+1 , max(numbers) ) )
```

```python
#최대값 구하는 로직 버전
n=int(input())
for i in range(n):
    numbers=list(map(int,input().split(' ')))
    temp = numbers[0]
    for number in numbers:
        if number > temp:
            temp=number
    else:
        print('#{0} {1}'.format( i+1 ,temp ) )
```

### 2070.큰 놈, 작은 놈, 같은 놈

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```python
n = int(input())
for i in range(n):
    numbers = list(map(int,input().split(' ')))
    if numbers[0]>numbers[1] :
        print('#{} {}'.format(i+1,'>'))
    elif numbers[0]==numbers[1] :
        print('#{} {}'.format(i+1,'='))
    else:
        print('#{} {}'.format(i+1,'<'))
```

### 2071.평균값 구하기

10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
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
n = int(input())
for i in range(n):
    numbers = list(map(int,input().split(' ')))
    result=0
    for number in numbers:
        result += number
        round_result = round (result / 10)
    print('#{} {}'.format(i+1, round_result))
```

### 2072.홀수만 더하기

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

#### enumerate()를 활용할수 있을듯한데... 나중에 해볼까

```python
n = int(input())
numbers = []
for i in range(n):
    numbers = list(map(int,input().split(' ')))
    result = 0
    for number in numbers:
        if number%2: #홀수
            result += number
    else:
        print('#{} {}'.format(i+1, result))
```

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

##아직 미해결

```python
n = int ( input() )
for i in range(n):
    numbers = list(map(int,input().split(' ')))
    cnt_numbers=dict()
    for i in range(1,101):
        cnt=0
        for number in numbers:
            if number == i :
                cnt+=1
        else: #i=1, cnt=i의 빈도값
            cnt_numbers[i] = cnt
    else: #1~100 최 빈도값 저장 완료
        result_num = 0 #최빈값
        result_cnt = 0 #최빈값의 최빈도수
        for idx,val in cnt_numbers.items():
            if val >= result_cnt : #동일값 >>> 나중에 온 값이 저장
                result_num = idx
                result_cnt = val
        #최빈값 출력
        print(result_num)
```