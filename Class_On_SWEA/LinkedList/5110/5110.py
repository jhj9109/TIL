import sys
sys.stdin = open('input5110.txt')

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

    def insert5110(self, thead, ttail, tsize):
        # insert 포인트 찾는 부분
        current = self.head
        i = 0
        while current is not None:
            if current.value > thead.value:
                break
            i += 1
            current = current.next
        # i : insert 타겟 포인트 

        if i == 0:
            # [ ] , <1> , 2 , 3
            if self.size == 0:
                self.head, self.tail = thead, ttail
                # thead.pre, ttail.next = None, None
            else:
                self.head.pre = ttail
                ttail.next = self.head
                self.head = thead
        elif i == self.size:
            # 1, 2, 3, [ ]
            self.tail.next = thead
            thead.pre = self.tail
            self.tail = ttail
        else:
            # 1, [ ], <2>
            thead.pre, ttail.next = current.pre, current
            current.pre.next, current.pre = thead, ttail
        self.size += tsize

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

def go(c):
    if c[0] == 'D':
        l.pop( int(c[1]) )
    elif c[0] == 'C':
        l.change( int(c[1]), int(c[2]) ) 
    elif c[0] == 'I':
        l.insert( int(c[1]), int(c[2]) )
    else:
        print('error')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    l = LinkedList()

    # 베이스 링크드리스트 생성
    for n in map(int, input().split()):
        l.push(n)

    # insert 부분
    for _ in range(M-1):
        temp = LinkedList()
        for v in list(map(int, input().split())):
            temp.push(v)
        l.insert5110( temp.head, temp.tail, temp.size )

    # 출력부분
    print(f'#{tc}', end=' ')
    print(*l.print(l.size-1, l.size-10))