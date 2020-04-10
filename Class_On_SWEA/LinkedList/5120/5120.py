import sys
sys.stdin = open('input5120.txt')
'''
창립 기념일
최대 10개인 비밀번호
N : 1000이하 숫자, 인덱스0에서 시작
M : 인덱스0에서 시작, M번째 칸에 생성
K : 회 반복.
마지막 숫자부터 10개까지만 출력
'''
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None
        self.pre = None

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    # 삽입 류
    def push(self, value):
        item = Node(value)
        if self.size == 0:
            self.head = self.tail = item
            # item.next, item.pre = None, None
        else:
            item.pre = self.tail
            self.tail.next = item
            self.tail = item
        self.size += 1

    def pushleft(self, value):
        item = Node(value)
        if self.size == 0:
            self.head = self.tail = item
            # item.next, item.pre = None, None
        else:
            item.next = self.head
            self.head.pre = item
            self.head = item
        self.size += 1

    def pick(self, idx):
        if idx < self.size//2:
            current = self.head
            for _ in range(idx):
                current = current.next
            return current.value
        else:
            current = self.tail
            for _ in range((self.size-1)-idx):
                current = current.pre
            return current.value

    def insert(self, idx, value):
        if idx == 0:
            self.pushleft(value)
        elif idx == self.size:
            self.push(value)
        else:
            item = Node(value) # 1에 넣기 (idx:0~9, size = 10 >>> 9) : 7, 8, item, <9>
            if idx < self.size//2:
                current = self.head
                for _ in range(idx):
                    current = current.next
                item.pre, item.next = current.pre, current
                current.pre.next, current.pre = item, item
            else:
                current = self.tail
                for _ in range(self.size-(idx+1)):
                    current = current.pre
                item.pre, item.next = current.pre, current
                current.pre.next, current.pre = item, item
            self.size += 1

    def print(self, start, end):
        if start < self.size//2:
            current = self.head
            for _ in range(start):
                current = current.next
        else:
            current = self.tail
            for _ in range((self.size-1)-start):
                current = current.pre
        # start: current
        ret_lst = [current.value]
        if start <= end:
            for _ in range(end-start):
                current = current.next
                if current is None:
                    break
                ret_lst.append(current.value)
        else:
            for _ in range(start-end):
                current = current.pre
                if current is None:
                    break
                ret_lst.append(current.value)
        return ret_lst
                

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    l = LinkedList()
    for v in list(map(int, input().split())):
        l.push(v)
    i = 0
    # 시작 숫자
    start_num = l.pick(i)
    for _ in range(K):
        # 시작칸 i에서 M번째칸, 앞으로 넘어가는 로직 포함
        i = i+M-l.size if i+M > l.size else i+M
        # 밀려나는 칸이 없으면, 시작숫자와 더함
        if i == l.size:
            l.insert(i, l.pick(l.size-1) + start_num)
        else:
            l.insert(i, l.pick(i-1) + l.pick(i))
    # 출력
    lst = l.print(l.size-1, l.size-10)
    print(f'#{tc} ', end='')
    print(*lst, end=' ')
    print('')