''' Author : Abdallah rabie
Sec: 2
Q17) write a python class that implement the function of Queue

'''


class Queue:

    def __init__(self):
        self.elements = []

    def queue(self, item):
        '''
            @param:  item to be added to the queue list
        '''
        self.elements.insert(0, item)

    def dequeue(self):
        return self.elements.pop()


queue = Queue()
queue.queue('add element 1')
queue.queue('add element 2')
queue.queue('add element 3')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
