class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        return True

    def dequeue(self):
        self.queue.pop(0)
        return True

    def size(self):
        return len(self.queue)

    def read(self):
        return self.queue[0]


TheQueue = Queue()
TheQueue.enqueue("Mon")
TheQueue.enqueue("Tue")
TheQueue.enqueue("Wed")
print(TheQueue.size())


class Deque:
    def __init__(self):
        self.deque = []
        self.end = len(self.deque) - 1

    def enqueue_left(self, data):
        self.deque.insert(0, data)
        return f'{data} added to front of deque'

    def enqueue_right(self, data):
        self.deque.append(data)
        return f'{data} added to end of deque'

    def dequeue_left(self):
        self.deque.pop(0)
        return 'front element dequeued'

    def dequeue_right(self):
        self.deque.pop()
        return 'end element dequeued'

    def read_front(self):
        return self.deque[0]

    def read_end(self):
        return self.deque[self.end]

    def size(self):
        return len(self.deque)


TheDeque = Deque()
TheDeque.enqueue_left("Mon")
TheDeque.enqueue_right("Tue")
TheDeque.enqueue_left("Wed")
