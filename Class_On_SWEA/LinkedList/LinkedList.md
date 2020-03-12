# Linked List
## 01 Linked List
### ⅰ. 리스트
- 순서를 가진 데이터의 묶음
- 시퀀스 자료형 - 인덱싱, 슬라이싱, 연산자, 메서드
- 크기제한, 타입제한 없음
- 동적 배열로 작성된 순차 리스트 >>> 삽입 삭제 연산에 많은 작업 필요
#### 리스트 복사
new_list =
- old_list : 얕은 복사
- old_list[:] : 슬라이싱
- new_list.extend(old_list) : extend()
- list(old_list) : list()
- copy.copy(old_list) : import copy
- [x for x in old_list] : 리스트함축
- copy.deepcopy : 리스트 원소까지도 깊은 복사

### ⅱ. 연결리스트
> 개별적으로 위치한 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룸
> 순차 리스트에서 물리적인 순서를 맞추기 위한 작업이 불필요
> 자료구조의 크기를 동적으로 조정할 수 있어, 메모리의 효율적인 사용 가능
> 순차탐색

#### 연결리스트 주요 함수
- addtoFirst(item)
- addtoLast(item)
- add(idx, item)
- delete(idx)
- get(idx)

#### 노드
> 연결리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료 단위
- 데이터 필드 : 원소의 값을 저장하는 자료구조
- 링크 필드 : 다음 노드의 주소를 저장하는 자료구조

#### 헤드
> 리스트의 처음 노드를 가리키는 레퍼런스

### ⅲ. 단순 연결리스트
> 노드가 하나의 링크 필드에 의해 다음 노드와 연결
> 헤드는 가장 앞의 노드, 최종 노드는 None을 가리킴

**삽입**
1. 메모리 할당하여 새로운 노드 new 생성
2. new의 데이터 필드에 '값' 저장
3. 삽입될 위치(i)에 있던 노드의 주소를 new의 링크 필드에 복사
4. (i-1) 노드의 링크 필드에 new의 주소를 복사

```python
def addtoFirst(data): # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head) # 새로운 노드 생성

def add(pre, data): # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
def addtoLast(data): # 마지막에 데이터 삽입
    global Head
    if Head == None: # 빈 리스트 이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: #마지막 노드 찾을때까지
            p = p.link
        p.link = Node(data, None)
```

**삭제**
1. 삭제할 노드의 선행 노드 탐색
2. 삭제할 노드의 링크 필드를 선행노드의 링크 필드에 복사

```python
def deletetoFirst(): # 처음 노드 삭제
    global Head
    if Head == None: # 빈 리스트 이면
        print('error')
    else:
        Head = Head.link

def delete(pre): # pre 다음 노드 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
```

### ⅳ. 이중 연결 리스트
> 양쪽 방향으로 순회가능 >>> 링크필드 1개 추가
**삽입**
1. 메모리를 할당하여 새로운 노드 new를 생성하고 데이터 필드에 '값' 저장
2. new.next = Node[i-1].next
3. Node[i-1].next = new
4. new.prev = Node[i-1]
5. Node[i].prev = new

**삭제**
1. Node[i-1].next = Node[i+1]
2. Node[i+1].prev = Node[i-1]

## 02 삽입 정렬
> 비교와 교환 알고리즘, O(n^2)
> n의 갯수가 작을 때 효과적

1. 정렬된 원소 S, 정렬되지 않은 원소 U
2. u가 공집합이 될때까지 u에서 s로 1개씩 삽입 정렬한다

## 03 병합 정렬
> 분할 정복 알고리즘, O(n log n)
> Top-Down 방식
> 연결 List의 경우 가장 효율적인 방식

1. 1개짜리 원소가 될때까지 전체 집합을 부분집합으로 나눔
2. 나눠진 부분집합이 1개의 전체 집합이 될때까지 병합

```python
def merge_sort(m):
    if len(m) <= 1: # 사이즈가 0,1인 경우 바로 리턴
        return m
    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER 부분 : 분할된 리스트를 병합
    return merge(left, right)
def merge(left, right):
    result = [] # 두개의 분할된 리스트를 병합하여 result를 만듬

    while len(left) > 0 and len(right) > 0: # 양쪽리스트에 원소가 남아 있는 경우
        # 두 서브 리스트의 첫 원소들을 비교하여 작은 것 부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0: # 왼쪽 리스트에 원소가 남아 있는 경우
        result.extend(left)
    if len(right) > 0: #오른쪽 리스트에 원소가 남아 있는 경우
        result.extend(right)
    # 각 리스트는 이미 정렬 된 상태 >>> 남은 원소 모두 extend 가능함
    return result
```
## 04 Linked List의 활용

### ⅰ. List를 이용한 stack

스택의 원소 : 리스트의 노드
- 스택 내의 순서는 리스트의 링크를 통해 연결
- Push : 리스트의 마지막 노드에 삽입
- Pop : 리스트의 마지막 노드 반환/삭제

변수 Top
- 리스트의 마지막 노드를 가리키는 변수
- 초기 상태 : Top = None

Push와 Pop 연산 구현
1. None값을 가지는 노드 만들어 스택 초기화
2. push(A) : A.next = None >>> Top = A, 
3. push(B) : B.next = Top >>> Top = B
4. push(C) : C.next = Top >>> Top = C
5. pop() : Top = C.next

```python
def push(i): # 원소 i를 스택 top(맨앞) 위치에 push
    global top
    top = Node(i, top) # 새로운 노드 생성
def pop():
    global top
    if top == None: # 빈 리스트이면
        print('error')
    else:
        data = top.data
        top = top.link # top이 가리키는 노드를 바꿈
        return data
```

우선순위 Queue
우선순위 큐의 구현과 기본 연산
구현 : 연결 리스트를 이용한 우선순위 큐
기본 연산 : 삽입 enQueue, 삭제 deQueue

순차 리스트를 이용한 우선순위 큐 구현
- 순차 리스트를 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨
문제점
- 배열을 사용, 삽입과 삭제 연산시 원소의 재배치 과정에서 소요되는 시간과 메모리 낭비

연결 리스트를 이용한 우선순위 큐 구현
- 연결 리스트를 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨
배열 대비 장점
- 삽입, 삭제 연산 이후 원소의 재배치 불필요
- 메모리의 효율적인 사용이 가능