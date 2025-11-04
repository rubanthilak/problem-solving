class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
    
    def swap(self, x, y):
        temp = self.arr[x]
        self.arr[x] = self.arr[y]
        self.arr[y] = temp 
                
    def sort(self):
        for i in range(0, self.n - 1):
            minIdx=i
            for j in range(i+1, self.n):
                if self.arr[j] < self.arr[minIdx]:
                    minIdx=j
            if i != minIdx:
                self.swap(i, minIdx)             

if __name__ == '__main__':
    arr = SelectionSort([2,7,4,5,1,3])
    arr.sort()
    print(arr.arr)