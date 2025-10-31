class ArrayStack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.cap = cap
        self.top = -1
    
    def push(self, data):
        if self.top == self.cap - 1:
            print("Stack is full")
            return 
        
        self.top +=1
        self.arr[self.top] = data
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        
        value = self.arr[self.top]
        self.top -=1
        return value
        
    def print(self):
        itr = self.top
        while itr > -1:
            print(self.arr[itr])
            itr -= 1
        
    def isEmpty(self):
        return self.top == -1