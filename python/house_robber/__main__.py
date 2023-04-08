from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0

        for n in nums:
            temp = max(n + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    

class TestSolution(unittest.case.TestCase):
    def test_rob(self):
        self.assertEqual(Solution().rob([1,2,3,1]),4)
        self.assertEqual(Solution().rob([2,7,9,3,1]),12)

if __name__ == '__main__':
    unittest.main()