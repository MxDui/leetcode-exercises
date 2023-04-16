from typing import List
import heapq
import unittest

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i] -=1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True
    

class TestSolution(unittest.TestCase):
    def test_isNStraightHand(self):
        self.assertEqual(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8],3),True)
        self.assertEqual(Solution().isNStraightHand([1,2,3,4,5],4),False)
       

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)