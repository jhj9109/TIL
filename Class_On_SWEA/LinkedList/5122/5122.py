import sys
sys.stdin = open('input5122.txt')

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

    def popright(self):
        ret = self.tail.value
        if self.size == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None
        self.size -= 1
        return ret

    def popleft(self):
        ret = self.head.value
        if self.size == 1:
            self.tail = self.head = None
        else:
            self.head = self.head.next
            self.head.pre = None
        self.size -= 1    
        return ret

    def pop(self, idx=None):
        if idx == None or idx == self.size-1:
            self.popright()
        elif idx == 0:
            self.popleft()
        else:
            if idx < self.size//2:
                current = self.head
                for _ in range(idx):
                    current = current.next
            else:
                current = self.tail
                for _ in range((self.size-1)-idx):
                    current = current.pre

            current.pre.next = current.next
            current.next.pre = current.pre
            self.size -= 1
            return current.value

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

    def change(self, idx, value):
        if idx < self.size//2:
            current = self.head
            for _ in range(idx):
                current = current.next
            current.value = value
        else:
            current = self.tail
            for _ in range((self.size-1)-idx):
                current = current.pre
            current.value = value
            # print(f'c:{current.value}, p:{self.pick(idx)}')

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

    def show(self):
        current = self.head
        if not current:
            print(None)
        else:
            print('size:',l.size, current.value, end=' ')
            while current.next:
                current = current.next
                print(current.value, end=' ')
        print('')

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
    N, M, L = map(int, input().split())
    d = list(map(int, input().split()))
    l = LinkedList()
    for v in d:
        l.push(v)
    for _ in range(M):
        go(input().split())
    if l.size <= L:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {l.pick(L)}')