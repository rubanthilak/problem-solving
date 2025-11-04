class InsertionSort:
    def __init__(self, arr):
        self.arr=arr
        self.n=len(arr)
            
    def sort(self):
        for i in range(1, self.n):
            value = self.arr[i]
            for j in range(i-1, -1, -1):
                if self.arr[j] > value:
                    self.arr[j+1] = self.arr[j]
                    self.arr[j] = value
                else:
                    break
        return self
    
    def print(self):
        print(self.arr)

if __name__ == '__main__':
    arr = InsertionSort([2,7,4,5,1,3])
    arr.sort().print()