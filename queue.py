class Node:

    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self):
        new_node = Node()
        a = int(input("\nEnter the data for node :"))
        new_node.data = a
        if(self.head==None):
            self.head = new_node
            print("Initially Head and Tail are pointing to : %d " % self.head.data )
            return

        last = self.head
        while(last.next!=None):
            last = last.next

        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        print("Tail is pointing to : %d " % self.tail.data )

    def printqueue(self):

        if self.head==None :
            print("\nQueue is Empty")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse(self):
        temp = self.tail
        while(temp):
            print(temp.data)
            temp = temp.prev
    
    def headtail(self):
        print("Head : %d " % self.head.data)
        print("Tail : %d " % self.tail.data)

    def dequeue(self):

        if(self.head==None):
            print("\nQueue is empty !!")
            return

        print("\nHead is pointing to %s " % self.head.data)
        print("\n%d is dequeued from the Queue. " % self.head.data)
        temp = self.head
        self.head = temp.next
        temp=None
       # return

if __name__ == "__main__":
    q1 = Queue() 
    for i in range(0,6):
        q1.enqueue()
    q1.printqueue()
    print("\nThe values of head and tail are :")
    q1.headtail()
    q1.reverse()
    for i in range(0,6):
        q1.dequeue()
    q1.printqueue()
    