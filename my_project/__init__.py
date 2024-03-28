import math
import element_controller as ec
import geometry_controller as gc
import cadwork

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("What is happening?")


class FooDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Something is happening before the function is called.")
        self.func()
        print("Something is happening after the function is called.")

@FooDecorator
class WhatIsHappening:
    def __init__(self):
        print("i am initing")


def matrix_multiply(matrix, point):
    result = cadwork.point_3d(0, 0, 0)
    for i in range(len(matrix)):
        for j in range(3): # len(point)
            result[i] += matrix[i][j] * point[j]
    # result = [sum(m*p for m, p in zip(row, point)) for row in matrix]
    return result




if __name__ == "__main__":
    print("Hello world")
    say_whee()
    my_cls = WhatIsHappening()

    element_ids = ec.get_active_identifiable_element_ids()

    # face vertices
    # points = [
    #     [0.000000, 0.000000, 0.000000],
    #     [0.000000, 1000.000000, 0.000000],
    #     [1000.000000, 1000.000000, 0.000000],
    #     [1000.000000, 0.000000, 0.000000]
    # ]
    points = gc.get_element_vertices(*element_ids)
    angle = math.radians(90)

    # rotate around y-axis
    rotation_matrix = [
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ]

    # Rotation matrix around the x-axis
    # rotation_matrix = [
    #     [1, 0, 0],
    #     [0, math.cos(angle), -math.sin(angle)],
    #     [0, math.sin(angle), math.cos(angle)]
    # ]

    rotated_points = [matrix_multiply(rotation_matrix, point) for point in points]

    print(rotated_points)

    ec.create_surface(rotated_points)
