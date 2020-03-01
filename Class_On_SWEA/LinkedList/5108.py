import sys
sys.stdin = open('input5108.txt')
'''
7:05~7:50
N개의 10억 이하 자연수 수열.
'''
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, idx, value):
        item = Node(value)
        current = self.head
        if idx == 0:
            item.next = current
            self.head = item
        else:
            for _ in range(idx-1):
                current = current.next
            item.next = current.next
            current.next = item

    def push(self, value):
        item = Node(value)
        current = self.head
        if not current:
            self.head = item
        else:
            while current.next:
                current = current.next
            current.next = item
    def show(self):
        current = self.head
        if not current:
            print(None)
        else:
            print(current.value)
            while current.next:
                current = current.next
                print(current.value)
    def pick(self, idx):
        current = self.head
        if idx == 0:
            return current.value
        else:
            for _ in range(idx):
                current = current.next
            return current.value

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 수열길이N, 추가횟수M, 출력인덱스L
    
    d1 = list(map(int, input().split())) # 길이:N
    d2 = [list(map(int, input().split())) for _ in range(M)]

    s = LinkedList()
    for i in d1:
        s.push(i)
    for i, v in d2:
        s.insert(i, v)
    print(f'#{tc} {s.pick(L)}')