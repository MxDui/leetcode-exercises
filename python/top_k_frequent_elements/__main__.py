from typing import List
import unittest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
class TestSolution(unittest.TestCase):
    def test_topKFrequent(self):
        solution = Solution()

        self.assertEqual(solution.topKFrequent([1,1,1,2,2,3], 2), [1,2])
        self.assertEqual(solution.topKFrequent([1], 1), [1])

if __name__ == '__main__':
    unittest.main()