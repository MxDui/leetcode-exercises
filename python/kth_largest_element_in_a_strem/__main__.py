import heapq
import unittest
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class Test(unittest.TestCase):
    def test1(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kthLargest.add(3), 4)
        self.assertEqual(kthLargest.add(5), 5)
        self.assertEqual(kthLargest.add(10), 5)
        self.assertEqual(kthLargest.add(9), 8)
        self.assertEqual(kthLargest.add(4), 8)

    def test2(self):
        kthLargest = KthLargest(1, [])
        self.assertEqual(kthLargest.add(-3), -3)
        self.assertEqual(kthLargest.add(-2), -2)
        self.assertEqual(kthLargest.add(-4), -2)
        self.assertEqual(kthLargest.add(0), 0)
        self.assertEqual(kthLargest.add(4), 4)

    def test3(self):
        kthLargest = KthLargest(2, [0])
        self.assertEqual(kthLargest.add(-1), -1)
        self.assertEqual(kthLargest.add(1), 0)
        self.assertEqual(kthLargest.add(-2), 0)
        self.assertEqual(kthLargest.add(-4), 0)
        self.assertEqual(kthLargest.add(3), 1)


if __name__ == "__main__":
    unittest.main()
