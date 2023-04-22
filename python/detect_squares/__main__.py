from collections import defaultdict
from typing import List
import unittest

class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)



class Test(unittest.TestCase):
    def test_DetectSquares(self):
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])
        self.assertEqual(detectSquares.count([11, 10]), 1)
        self.assertEqual(detectSquares.count([14, 8]), 0)
        detectSquares.add([11, 2])
        self.assertEqual(detectSquares.count([11, 10]), 2)

if __name__ == "__main__":
    unittest.main()