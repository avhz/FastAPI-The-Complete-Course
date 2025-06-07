import random


class Point:
    def __init__(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)

    def is_inside_circle(self):
        return self.x**2 + self.y**2 <= 1

    def generate_points(self, n):
        return [Point() for _ in range(n)]


class MonteCarloPi:
    def __init__(self, n):
        self.n = n

    def run(self) -> float:
        points = Point().generate_points(self.n)
        inside = sum([1 for point in points if point.is_inside_circle()])
        return 4 * inside / self.n


if __name__ == "__main__":
    n = 10_000_000
    mcp = MonteCarloPi(n)
    print(mcp.run())


import numpy


class MonteCarloPi:
    def __init__(self, n):
        self.n = n

    def run(self) -> float:
        rng = numpy.random.default_rng()
        x = rng.uniform(-1, 1, self.n)
        y = rng.uniform(-1, 1, self.n)
        inside = numpy.count_nonzero(x**2 + y**2 <= 1)
        return 4 * inside / self.n


if __name__ == "__main__":
    n = 100_000_000
    mcp = MonteCarloPi(n)
    print(mcp.run())
