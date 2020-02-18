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
    
    def delete(self, position):
        current = self.head
        for _ in range(1, position-1):
            current = current.next
        current.next = current.next.next
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
l = LinkedList(n1)
l.append(n2)
# l.show2()
# print('')
l.insert(n3, 2)
l.show2()
print('')
l.delete(1)
l.show2()
