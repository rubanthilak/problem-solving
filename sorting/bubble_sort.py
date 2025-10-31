class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        
    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
        
    def sort(self):
        for i in range(0, self.n-1):
            flag=0
            for j in range(0, self.n - (i + 1)):
                if(self.arr[j] > self.arr[j+1]):
                    self.swap(j, j+1)
                    flag=1
            if flag == 0:
                break
            
            
if __name__ == '__main__':
    arr=[2,7,4,5,1,3]
    bs = BubbleSort(arr)
    bs.sort()
    print(bs.arr)
            