class Pari:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair({0.x!r}, {0.y!r})".format(self)
