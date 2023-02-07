import heapq
from typing import List
import unittest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)

        return abs(stones[0])


class TestSolution(unittest.TestCase):
    def test_lastStoneWeight(self):
        self.assertEqual(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)

    def test_lastStoneWeight2(self):
        self.assertEqual(Solution().lastStoneWeight([2, 2]), 0)

    def test_lastStoneWeight3(self):
        self.assertEqual(Solution().lastStoneWeight([1, 3]), 2)


if __name__ == '__main__':
    unittest.main()
