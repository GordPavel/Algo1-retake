from main import count_collisions, Rectangle, Point

assert count_collisions([
    Rectangle(Point(1, 1), 2, 2, Point(0, 0)),
    Rectangle(Point(5, 5), 2, 2, Point(0, 0)),
], 1) == [0], 'No collisions'

assert count_collisions([
    Rectangle(Point(1, 1), 2, 2, Point(0, 0)),
    Rectangle(Point(3, 3), 2, 2, Point(0, 0)),
], 1) == [1], 'One border collision'

assert count_collisions([
    Rectangle(Point(1, 1), 2, 2, Point(0, 0)),
    Rectangle(Point(2, 2), 2, 2, Point(0, 0)),
], 1) == [1], 'Overlapping collision'

assert count_collisions([
    Rectangle(Point(1, 1), 10, 10, Point(0, 0)),
    Rectangle(Point(2, 2), 2, 2, Point(0, 0)),
], 1) == [1], 'Inside collision'

assert count_collisions([
    Rectangle(Point(1, 1), 2, 3, Point(0, 0)),
    Rectangle(Point(0, 1), 3, 1, Point(0.5, 1)),
    Rectangle(Point(0.5, 3), 0.3, 0.5, Point(0, 0)),
], 2) == [1, 2], 'Moving rectangles'
