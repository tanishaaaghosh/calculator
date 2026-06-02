class Cursor:
    def __init__(self, items):
        self.items = items
        self.pos = 0

    def current(self):
        if self.pos < len(self.items):
            return self.items[self.pos]
        return None

    def next(self):
        self.pos += 1

    def peek(self):
        if self.pos + 1 >= len(self.items):
            return None
        return self.items[self.pos + 1]