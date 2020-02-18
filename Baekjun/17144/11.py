class LinkedList: #인덱싱 불가.
    def __init__(self, head=None): #head가 있으면 카운팅도 편하고, 시작점으로 가기가 편하다.
        self.head = head

    def append(self, data):
        self.head.next = data
    
    
    def lprint(self):
        print(self.head)
n1 = Node(5)
l = LinkedList(n1)

l.lprint()