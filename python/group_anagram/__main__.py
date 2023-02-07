from typing import List
import unittest
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch)-ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


class TestSolution(unittest.TestCase):
    def test_groupAnagrams(self):
        self.assertEqual(set(map(tuple, Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))),
                         set([("tan", "nat"), ("bat",), ("eat", "tea", "ate")]))
    def test_groupAnagrams2(self):

        self.assertEqual(list(Solution().groupAnagrams([""])), [[""]])

    def test_groupAnagrams3(self):
        self.assertEqual(list(Solution().groupAnagrams(["a"])), [["a"]])


if __name__ == '__main__':
    unittest.main()
