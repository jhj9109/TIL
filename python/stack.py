class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    def insert_front(self, item):
        current = self.head
        item.next = current
        self.head = item

    ##delete_front()
    def delete_front(self):
        current = self.head
        if current:
            self.head = current.next
            return current.value

class Stack(LinkedList):
    def push(self, item):
        super().insert_front(item)
    
    def pop(self):
        return super().delete_front()