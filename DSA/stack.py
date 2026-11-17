
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. PUSH
    def push(self, data):
        NewNode = Node(data)

        if self.isempty():
            self.top = NewNode
            NewNode = self.top
        else:
            NewNode.next = self.top
            self.top = NewNode

    # 2. POP
    def pop(self):
        if self.isempty():
            print("Stack is Underflow")
        else:
            curr = self.top
            self.top = self.top.next
            curr = None

    # 3. DISPLAY
    def print_stack(self):
        if self.isempty():
            print("Stack is Empty")
            return

        curr = self.top

        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next

        print()

    # 4. REVERSE STRING USING STACK
    def reverse_string(self):
        string = input("Enter a string: ")

        NewStack = stack()

        for ch in string:
            NewStack.push(ch)

        reverse = ""

        while not NewStack.isempty():
            reverse += NewStack.top.data
            NewStack.pop()

        print("Reversed String:", reverse)

    # 5. REVERSE STACK USING ANOTHER STACK
    def reverse(self):
        curr = self.top

        while curr != None:
            NewStack.push(curr.data)
            curr = curr.next


# MAIN PROGRAM

s = stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Original Stack:")
s.print_stack()

s.pop()

print("After Pop:")
s.print_stack()


# Reversing Stack using New Stack

NewStack = stack()

s.reverse()

print("Reversed Stack:")
NewStack.print_stack()

# Reverse String
s.reverse_string()