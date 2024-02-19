"""
Stack / Array
Troy Brunette
CS240

Implement a stack for both a Linked List & Array. Use your HW 1 implementation of a Linked List.

    Push
    Pop
    IsEmpty
    IsFull
    Peek
"""


class Stack:
    def __init__(self, size=None):  # Constructor for Stack
        if size is not None:
            self.items = [None] * size
            self.max_size = size
        else:
            self.items = []
            self.max_size = size

    # Push adds an item to the top of the Stack; except if the Stack is full
    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print(f"Can't add {item} to a full stack! ")

    # Pop removes from the top of the stack
    def pop(self):
        if not self.is_empty():  # If stack is not empty we Pop
            return self.items.pop()
        else:
            print("Can't Pop! ~ Stack is Empty!")

    # Returns True if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Returns True if the Stack is full by checking size of array to the max Stack size
    def is_full(self):
        if len(self.items) == self.max_size and self.items[-1] is not None:
            return True
        else:
            return False

    # Peek looks at the top item
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Using -1 removes the last element in a python list
        else:
            print("Can't Peek! ~ Stack is Empty")

    def size(self):
        return len(self.items)


# Testing Stack functions
# array_stack = Stack(4)
# array_stack.push(1)
# print("Top element:", array_stack.peek())
#
# array_stack.push(2)
#
# print("Take a PEEK at the top of the stack:", array_stack.peek())
# print("Popped item: ", array_stack.pop())
#
# print("Is the stack full?", array_stack.IsFull())
#
# print("Stack size is: ", array_stack.size())
# array_stack.push(3)
# array_stack.push(4)
# array_stack.push(5)
# print("Stack size:", array_stack.size())
# print("Is the stack full?", array_stack.IsFull())
#
#
# array_stack.push(6)  # Can't Push 6 on to Stack because it's full
# print("Take a PEEK at the top of the stack:", array_stack.peek())
# print("Popped item: ", array_stack.pop())
# print("Popped item: ", array_stack.pop())
# print("Popped item: ", array_stack.pop())
# print("Popped item: ", array_stack.pop())
#
# array_stack.pop()  # Can't Pop because the stack is now empty

#
# print("Stack size:", array_stack.size())
# print("Is the stack full?", array_stack.IsFull())
#
# array_stack2 = Stack()
# array_stack2.push(1)
# array_stack2.push(2)
# array_stack2.push(3)
# array_stack2.push(4)
# print("Take a PEEK at the top of the stack:", array_stack2.peek())
# print("Popped item: ", array_stack2.pop())
# array_stack2.push(4)
#
# array_stack2.push(4)
# print("Is the stack full?", array_stack2.IsFull())
#
# print("Stack size is: ", array_stack2.size())
