
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # CHECK EMPTY
    def isempty(self):
        return self.front is None

    # 1. ENQUEUE
    def enqueue(self, data):
        NewNode = Node(data)

        if self.isempty():
            self.front = NewNode
            self.rear = NewNode
        else:
            self.rear.next = NewNode
            self.rear = NewNode

    # 2. DEQUEUE
    def dequeue(self):
        if self.isempty():
            print("Queue is Underflow")
        else:
            curr = self.front
            print("Deleted element:", curr.data)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

            curr = None

    # 3. DISPLAY
    def print_queue(self):
        if self.isempty():
            print("Queue is Empty")
        else:
            curr = self.front

            while curr != None:
                print(curr.data, end=" ")
                curr = curr.next

            print()

    # 4. REVERSE QUEUE USING STACK
    def reverse(self):
        NewStack = []

        curr = self.front

        while curr != None:
            NewStack.append(curr.data)
            curr = curr.next

        self.front = None
        self.rear = None

        while len(NewStack) > 0:
            self.enqueue(NewStack.pop())

        print("Queue Reversed")

    # 5. MERGE TWO QUEUES
    def merge(self, q2):
        curr = q2.front

        while curr != None:
            self.enqueue(curr.data)
            curr = curr.next

    # 6. CHECK IDENTICAL QUEUES
    def identical(self, q2):
        curr1 = self.front
        curr2 = q2.front

        while curr1 != None and curr2 != None:

            if curr1.data != curr2.data:
                print("Queues are not identical")
                return

            curr1 = curr1.next
            curr2 = curr2.next

        if curr1 == None and curr2 == None:
            print("Queues are identical")
        else:
            print("Queues are not identical")


# MAIN PROGRAM

q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)

print("Original Queue:")
q1.print_queue()

# Dequeue
q1.dequeue()

print("After Dequeue:")
q1.print_queue()

# Reverse Queue
q1.reverse()

print("Reversed Queue:")
q1.print_queue()

# Create Second Queue
q2 = Queue()

q2.enqueue(100)
q2.enqueue(200)
q2.enqueue(300)

# Merge Queues
q1.merge(q2)

print("Merged Queue:")
q1.print_queue()

# Check Identical Queues
q3 = Queue()

q3.enqueue(50)
q3.enqueue(40)
q3.enqueue(30)
q3.enqueue(20)

q1.identical(q3)
