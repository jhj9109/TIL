class Node():
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

class Queue_Linked_list():
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, item):
        if self.isEmpty():
            self.front = item
        else:
            self.rear.next = item
        self.rear = item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue_Empty")
            return None
        item = self.front.item
        self.front = self.front.next
        if self.isEmpty():
            rear = None
        return item
    
    def isEmpty(self):
        return self.front == None
    
    def Qpeek(self):
        return self.front.item
    
    def delete(self):
        if isEmpty():
            print("Queue_Empty")
        else:
            self.front = self.front.next
    
    def printQ(self):
        f = self.front
        s = ""
        while f:
            s += f.item + ""
            f = f.next
        return s