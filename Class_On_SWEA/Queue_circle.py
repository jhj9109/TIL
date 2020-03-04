class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue_circle():
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.size = size
        self.queue = [None for _ in range(self.size)]
    # def createQueue():
    #     pass

    def enQueue(self, item):
        if self.isFull():
            print("Queue_Full")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue_Empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == self.rear
    
    def Qpeek(self):
        if isEmpty():
            print("Queue_Empty")
        else:
            return self.queue[front+1]
    
    def delete(self):
        if isEmpty():
            print("Queue_Empty")
        else:
            self.front = (self.front + 1) % self.size