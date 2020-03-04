class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue_list():
    def __init__(self):
        self.front = -1
        self.rear = len(queque) - 1
        self.queue = []
    # def createQueue():
    #     pass

    def enQueue(self, item):
        self.queue.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue_Empty")
        else:
            return self.queue.pop(0)
    
    def isEmpty(self):
        return not len(self.queues)
    
    def Qpeek(self):
        if isEmpty():
            print("Queue_Empty")
        else:
            return self.queue[0]
    
    def delete(self):
        if isEmpty():
            print("Queue_Empty")
        else:
            self.queue.pop(0)