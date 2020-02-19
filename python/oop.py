class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def append(self, item):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = item
        else:
            current = item
    
    def show(self):
        current = self.head
        if current:
            while current:
                print(current.value)
                current = current.next
        print(None)    #head = None이면 None 출력

    def show2(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    #head = None이면 아무것도 출력 X

    def insert(self, item, position):
        current = self.head
        for _ in range(1, position):
            current = current.next
        item.next = current.next
        current.next = item
    
    def delete_i(self, position):
        current = self.head
        for _ in range(1, position-1):
            current = current.next
        current.next = current.next.next
    
    def delete_v(self, target):
        current = self.head
        if current.value == target: #첫번째 노드가 대상
            self.head = current.next
        else:
            while current.next != None:
                current = current.next
                if current.value == target: #두번째노드가 대상
                    current = current.next
    
    def size(self):
        current = self.head
        cnt = 0
        while current:
            cnt += 1
            current = current.next
        return cnt

    
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
l = LinkedList(n1)
l.append(n2)
l.insert(n3, 2)
l.show2()
print(f'size : {l.size()}')
