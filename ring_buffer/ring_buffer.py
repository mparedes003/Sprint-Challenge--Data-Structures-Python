class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # add an item to the buffer
    def append(self, item):

        for i in range(0, len(self.storage)):
            if self.storage[i] == None:
                self.storage[i] = item
                # print(f'PRINT AS ARRAY FILLS UP: {self.storage}')
                return
        # append item to the current oldest index
        self.storage[self.current] = item
        # if the current index is at the end of storage
        if self.current == len(self.storage) - 1:
            self.current = 0
        else:
            self.current += 1
            # print(
            # f'PRINT APPEND TO WHILE DROPPING CURRENT OLDEST INDEX:{self.storage}')

    # returns all of the elements in the buffer in a list in their given order
    # Don't return None value if present
    # Ring Buffer runs in 0.001 secs in O(n) time
    def get(self):
        items_in_buffer = []
        for item in self.storage:
            if item is not None:
                items_in_buffer.append(item)

        return items_in_buffer
