from typing import List
import unittest


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res


class UnitTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8])


if __name__ == "__main__":
    unittest.main()
