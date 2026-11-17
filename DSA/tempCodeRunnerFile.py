
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class Hospital:
    def __init__(self):
        self.front = None

   
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    
    def display_next(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Next Patient:", self.front.name)

    
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next

    
    def display(self):
        if self.front == None:
            print("Queue is empty")
            return

        temp = self.front

        while temp != None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next



patients = Hospital()


patients.enqueue(Node(11, "Atharv", 3))
patients.enqueue(Node(12, "Vansh", 1))
patients.enqueue(Node(13, "Tanaya", 2))

print("All Waiting Patients:")
patients.display()

print("\nNext Patient:")
patients.display_next()

print("\nAfter Treatment:")
patients.dequeue()

print("\nRemaining Patients:")
patients.display()

print("\nNext Patient:")
patients.display_next()

print("\nAfter Treatment:")
patients.dequeue()

print("\nRemaining Patients:")
patients.display()
