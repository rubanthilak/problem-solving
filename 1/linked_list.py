class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def insertAtStart(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtEnd(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new_node

    def insertAt(self, data, index) -> None:
        new_node = Node(data)
        position = 0
        itr = self.head
        
        if index == 0:
            self.insertAtStart(data)
            return
        
        while itr != None and position+1 != index:
            position += 1
            itr = itr.next
        
        if itr != None:
            new_node.next = itr.next
            itr.next = new_node
        else:
            print("Error: Index not present -", index, "\n")
            
    def removeFirst(self) -> None:
        itr = self.head
        if itr is None:
            print("Stack is empty")
        else:
            self.head = itr.next
    
    def removeLast(self) -> None:
        if self.head is None:
            print("Stack is empty")
        else:
            itr = self.head
            next_itr = itr.next
            while next_itr != None and next_itr.next != None:
                itr = next_itr
                next_itr = next_itr.next
            itr.next = None

    def remove(self, data) -> None:
        if self.head is None:
            print("Stack is empty")
            return
        
        itr = self.head
        while itr != None and itr.next != None and itr.next.data != data:
            itr = itr.next
        
        if itr is None:
            return
        
        if itr.next != None:
            itr.next = itr.next.next

    def printLinkedList(self) -> None:
        itr = self.head
        if itr is None:
            print("Stack is empty")
        else:
            print("|",  itr.data, "| <- *head")
            itr = itr.next
            while itr:
                print("|", itr.data, "|")
                itr = itr.next
            print("-----")
