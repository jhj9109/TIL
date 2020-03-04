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
l1 = LinkedList()
for i in range(0, 2+1):
    l1.push(i)

# l2 = LinkedList()
# for i in range(11, 12+1):
#     l2.push(i)
# l1.push_LikedList(l2)

# l1.show()
l2 = LinkedList()
print(l1.get_len())
print(l2.get_len())