from typing import List
from collections import Counter, deque
import heapq
import unittest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


class TestLeastInterval(unittest.TestCase):
    def test_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        out = 8
        self.assertEqual(Solution().leastInterval(tasks, n), out)

    def test_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        out = 6
        self.assertEqual(Solution().leastInterval(tasks, n), out)

    def test_3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        out = 16
        self.assertEqual(Solution().leastInterval(tasks, n), out)

    def test_4(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 1
        out = 12
        self.assertEqual(Solution().leastInterval(tasks, n), out)

    def test_5(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 0
        out = 12
        self.assertEqual(Solution().leastInterval(tasks, n), out)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
