'''
    Queue : A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).
            A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.The difference between
            stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

    Queue can be created by using both Singly and Doubly Linked list , in this implementation
    we will be using doubly linked list 

    Basically as stack queue also has two operations enqueue and dequeue.
    as Queue uses FIFO (First in First Out) the elements are removed based on their insertion order
    i.e if 1,2,3,4,5,6 are inserted in the Queue then 1 will be the element to be removed first and will continue accordingly

    Here in this we will maintain two pointers that are mainly head and tail

    the Enqueueing process will be done from tail and Dequeueing will be done from head

    Enqueueing : The process of adding elements 
    Dequeueing : The Process of removing elements

    Enqueuing :

    Initially both head and tail will point to a common Node :

             --------------
    head -> | data1 | next | <- tail
             --------------

    But as the Elements are added tail is shifted towards right (Enqueueing)

    # Step 1 :

             --------------      --------------
    head -> | data1 | next | -> | data2 | next | <- tail
             --------------      --------------

    # Step 2 :

             --------------      --------------      --------------
    head -> | data1 | next | -> | data2 | next | -> | data3 | next | <- tail
             --------------      --------------      --------------



    Dequeueing :

    This will start from left to right head will shift from Node to Node and will start removing 
    Nodes according to their Insertion Order .

    # Step 1 :

             --------------      --------------      --------------
    head -> | data1 | next | -> | data2 | next | -> | data3 | next | <- tail
             --------------      --------------      --------------

    # Step 2 : 

    As we can see data1 is removed from the Queue

                --------------      --------------      
    head -> -> | data2 | next | -> | data3 | next | <- tail
                --------------      --------------      

    # Step 3 :

              --------------           
    head  -> | data3 | next | <- tail
              --------------          


'''

# Initializing our Node that we will use
class Node:

    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None
# Initializing our Queue Class
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None


    # Function to Enqueue (Insertion) Elements in Queue
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

    # Function to Print Queue
    def printqueue(self):

        if self.head==None :
            print("\nQueue is Empty")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Function to Print the Queue in Reverse Order
    def reverse(self):
        temp = self.tail
        while(temp):
            print(temp.data)
            temp = temp.prev
    
    # Function that returns Head and Tail value
    def headtail(self):
        print("Head : %d " % self.head.data)
        print("Tail : %d \n" % self.tail.data)

    # Function to Dequeue (Removing) Elements from the Queue
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

# Main function 
if __name__ == "__main__":
    q1 = Queue() 
    for i in range(0,6):
        q1.enqueue()
    print("\nElement in queue are as follow:\n")
    q1.printqueue()
    print("\nThe values of head and tail are :\n")
    q1.headtail()
    q1.reverse()
    for i in range(0,6):
        q1.dequeue()
    q1.printqueue()