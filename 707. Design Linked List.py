from linkedlistfunc import LinkedListPrint
class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        curr = self.head
        findindex = 0

        # Empty list
        if self.head.val == -1:
            return -1

        while curr:
            if findindex == index:
                # print(curr.val)
                return curr.val

            findindex += 1
            curr = curr.next
        # print("Index out of range")
        return -1
    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head.val == -1:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
            return
        # LinkedListPrint(self.head)
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head.val == -1:
            self.head = node
            return
                
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        # LinkedListPrint(self.head)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            # LinkedListPrint(self.head)
            return
        if self.head.val == -1:
            return
        
        node = Node(val)
        curr = self.head
        findindex = 0

        while curr:
            if findindex == index-1:
                node.next = curr.next
                curr.next = node
                # LinkedListPrint(self.head)
                return
            findindex +=1
            curr = curr.next
        curr.next = node
        # LinkedListPrint(self.head)
 
    def deleteAtIndex(self, index: int) -> None:

        # Empty list
        if self.head.val == -1:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next

            # If list becomes empty
            if self.head is None:
                self.head = Node(-1)
            return

        curr = self.head
        findindex = 0

        while curr.next:

            if findindex == index - 1:
                curr.next = curr.next.next
                return

            curr = curr.next
            findindex += 1
        # LinkedListPrint(self.head)
        


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.deleteAtIndex(0)
myLinkedList.addAtTail(2)
myLinkedList.get(0)