from typing import List
import unittest

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair =[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


class Test(unittest.TestCase):

    def test_carFleet(self):
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]
        out = 3
        self.assertEqual(Solution().carFleet(target, position, speed),out)
        target = 10
        position = [0,4,2]
        speed = [2,1,3]
        out = 1
        self.assertEqual(Solution().carFleet(target, position, speed),out)
        


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)