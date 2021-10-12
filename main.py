class Point:
    def __init__(self, x, y):
        self.point = [x, y]

    def __getitem__(self, i):
        return self.point[i]

    def x(self):
        return self.point[0]

    def y(self):
        return self.point[1]


class Object:
    def __init__(self, velocity):
        self.velocity = velocity


class Rectangle(Object):
    def __init__(self, bot_left, width, height, velocity):
        super().__init__(velocity)
        self.bot_left = bot_left
        self.width = width
        self.height = height


def count_collisions(rects: [Rectangle], ticks: int) -> [int]:
    pass
