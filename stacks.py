#Next, let's do a little exercise. See if you can write your own stack() and queue() classes which add and remove elements as needed. Here are some hints - and don't overthink it. It's actually surprisingly simple to do.

#Remember that both stacks and queues are data structures.
#What common data structure will allow us to easily add and remove elements?
#Stacks are last in, first out, which means we need to add things to the end of the data structure and remove things from the end of the data structure.
#Queues are first in, first out, which means we need to add things to the end of the data structure and then remove things from the beginning of the data structure.

# Stack class implementation
class Stack:
    def __init__(self):
        # Initialize an empty list to store the elements of the stack
        self.items = []

    def push(self, item):
        # Add an item to the end of the list (last in)
        self.items.append(item)

    def pop(self):
        # Remove and return the last item from the list (last out)
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)


# Queue class implementation
class Queue:
    def __init__(self):
        # Initialize an empty list to store the elements of the queue
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the list (last in)
        self.items.append(item)

    def dequeue(self):
        # Remove and return the first item from the list (first out)
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of elements in the queue
        return len(self.items)


# Testing the Stack class
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Popped from stack:", stack.pop())
print("Popped from stack:", stack.pop())
print("Is stack empty?", stack.is_empty())

# Testing the Queue class
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Dequeued from queue:", queue.dequeue())
print("Dequeued from queue:", queue.dequeue())
print("Is queue empty?", queue.is_empty())
