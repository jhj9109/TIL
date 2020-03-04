class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.front = -1 
        self.rear = -1

    # def createQueue():
    #     pass

    def enQueue(self, item):
        if self.isFull():
            print("Queue_Full")
        else:
            self.rear += 1
            Q[self.rear] = item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue_Empty")
        else:
            self.front += 1
            return Q[self.front]
    
    def isFull(self):
        return self.rear == len(Q)-1
    
    def isEmpty():
        return self.front == self.rear
    
    def Qpeek():
        if isEmpty():
            print("Queue_Empty")
        else:
            return Q[front+1]