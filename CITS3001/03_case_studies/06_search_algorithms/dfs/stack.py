from StackEmptyError import StackEmptyError
# Since Python doesn't have a stack importation
class stack:
    def __init__(self):
        self.capacity = 10
        self.stack_ds = [None] * 10
        self.stack_size = 0

    def __len__(self):
        return self.stack_size

    def is_empty(self):
        return self.stack_size == 0

    def push(self, item):
        if self.stack_size == self.capacity:
            self._resize()

        self.stack_ds[self.stack_size] = item
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")

        popped = self.stack_ds[self.stack_size - 1]
        self.stack_ds[self.stack_size - 1] = None
        self.stack_size -= 1

        return popped

    def _resize(self):
        new_cap = self.capacity * 2
        new_stack = [None] * new_cap

        for i in range(self.stack_size):
            new_stack[i] = self.stack_ds[i]

        self.stack_ds = new_stack
        self.capacity = new_cap

    def top(self):
        return self.stack_ds[self.stack_size - 1]