import sys
sys.stdin = open('input5110.txt')
'''
7:56~9:25
나중 수열's 1st 보다 큰 값 앞에 끼워넣기
'''
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, arr):
        self.head = Node(arr[0])
        current = self.head
        for i in range(1, len(arr)):
            current.next = Node[arr[i]]


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

    def insert_Linkedlist(self, idx, item):
        current = self.head
        temp = item.get_last() # 맨마지막노드
        if not temp:
            print('error : 실행되지 못하였습니다.')
        else:
            if idx == 0:
                temp.next = current
                self.head = item.head
            else:
                for _ in range(idx-1):
                    current = current.next
                temp.next = current.next
                current.next = item.head

    def push(self, value):
        item = Node(value)
        current = self.head
        if not current:
            self.head = item
        else:
            while current.next:
                current = current.next
            current.next = item

    def get_len(self):
        current = self.head
        cnt = 0
        if not current:
            return cnt
        else:
            while current:
                current = current.next
                cnt += 1
            return cnt

    def push_LikedList(self, item):
        current = self.head
        if not current:
            self.head = item.head
        else:
            while current.next:
                current = current.next
            current.next = item.head

    def get_last(self):
        current = self.head
        if not current:
            return current
        else:
            while current.next:
                current = current.next
            return current # 맨 마지막 노드

    def show(self):
        current = self.head
        if not current:
            print(None)
        else:
            print(current.value)
            while current.next:
                current = current.next
                print(current.value)
    
    def nprint(self, n):
        current = self.head
        cnt = 0
        while cnt < n:
            print(current.value, end=' ')   
            current = current.next
            cnt += 1

    def pick(self, idx):
        current = self.head
        if idx == 0:
            return current.value
        else:
            for _ in range(idx):
                current = current.next
            return current.value

    def get_idx(self, value): #5110 문제용, 주어진 value보다 높은값 idx 리턴
        current = self.head
        idx = 0
        while current:
            if current.value > value:
                return idx
                break
            else:
                current = current.next
                idx += 1
        else:
            return idx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(M)]
    l1 = LinkedList()
    for n in d[0]:
        l1.push(n)
    for lst in d[1:]:
        l2 = LinkedList()
        for n in lst:
            l2.push(n)
        l1.insert_Linkedlist( l1.get_idx(lst[0]) , l2 )
    print(f'#{tc}', end = '') #0~len-1
    
    for i in range (1, 10+1):
        print(' ', end='')
        print(l1.pick(l1.get_len()-i), end = '')
    print('')