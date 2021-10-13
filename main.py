class Point:
    def __init__(self, x, y):
        self.point = [x, y]

    def __getitem__(self, i):
        return self.point[i]

    def x(self):
        return self.point[0]

    def y(self):
        return self.point[1]

    def __add__(self, other):
        return Point(self.x() + other.x(), self.y() + other.y())

    def __neg__(self):
        return Point(-self.x(), -self.y())

    def __sub__(self, other):
        return self.__add__(other.__neg__())


class Object:
    def __init__(self, velocity):
        self.velocity = velocity


class Rectangle(Object):
    def __init__(self, bot_left, width, height, velocity):
        super().__init__(velocity)
        self.bot_left = bot_left
        self.width = width
        self.height = height


def is_rectangles_collide(rect1: Rectangle, rect2: Rectangle):
    return rect1.bot_left.x() + rect1.width >= rect2.bot_left.x() and \
           rect1.bot_left.x() <= rect2.bot_left.x() + rect2.width and \
           rect1.bot_left.y() + rect1.height >= rect2.bot_left.y() and \
           rect1.bot_left.y() <= rect2.bot_left.y() + rect2.height


def count_collisions_for_tick(rects: [Rectangle]) -> int:
    collisions = 0
    for first_rect_iterator in range(len(rects)):
        for second_rect_iterator in range(first_rect_iterator):
            if is_rectangles_collide(rects[first_rect_iterator], rects[second_rect_iterator]):
                collisions += 1
    return collisions


def tick_rectangle(rect: Rectangle) -> Rectangle:
    return Rectangle(rect.bot_left + rect.velocity, rect.width, rect.height, rect.velocity)


def count_collisions(rects: [Rectangle], ticks: int) -> [int]:
    collisions = []
    for tick in range(ticks):
        tick_collisions = count_collisions_for_tick(rects)
        collisions.append(tick_collisions)
        rects = [tick_rectangle(rect) for rect in rects]
    return collisions
