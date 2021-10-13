from main import Rectangle, Point, count_collisions
from random import randint
from time import process_time
from datetime import timedelta


def rectangles_generator(count):
    for i in range(count):
        yield Rectangle(
            Point(randint(0, 1_000_000), randint(0, 1_000_000)),
            randint(0, 1_000_000),
            randint(0, 1_000_000),
            Point(randint(-1_000_000, 1_000_000), randint(-1_000_000, 1_000_000))
        )


rects = list(rectangles_generator(1000)), 10
start = process_time()
count_collisions(*rects)
stop = process_time()
time_for_1000 = stop - start
print(f'On 1000 rectangles solution works for {timedelta(seconds=time_for_1000)} time')

rects = list(rectangles_generator(2000)), 10
start = process_time()
count_collisions(*rects)
stop = process_time()
time_for_2000 = stop - start
print(f'On 2000 rectangles solution works for {timedelta(seconds=time_for_2000)} time')

print(f'If we double the task size, algorithm works {time_for_2000 / time_for_1000} times longer')
