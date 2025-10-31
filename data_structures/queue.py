class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None
        
class Queue:
    def __init__(self) -> None:
        self.head = None
        
    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            itr = self.head
            self.head = itr.next
    
    def print(self):
        if self.head is None:
            print("Queue is empty")
        else:
            itr = self.head
            print('|', itr.data, '|')
            while itr.next:
                print('|', itr.data, '|')
                itr = itr.next
    
    