class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.arr = [0] * size
        self.front = 0
        self.total = 0
        
    def enqueue(self, data):
        if self.total == self.size:
            print("Queue is full")
            return
        
        rear = (self.front + self.total) % self.size
        self.arr[rear] = data
        self.total += 1 
        
    def dequeue(self):
        if self.total == 0:
            print("Queue is empty")
            return
        
        nf = (self.front + 1) % self.size
        self.front = nf
        self.total -= 1
        
    def print(self):
        itr = self.front
        rear = (self.front + self.total) % self.size
        while itr < rear:
            print(self.arr[itr])
            itr = (itr + 1) % self.size
            
if __name__ == "__main__":
    q = CircularQueue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.enqueue(40)
    q.print()