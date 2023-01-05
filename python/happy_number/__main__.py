import unittest
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if  n == 1:
                return True
        
        return False 

    def sumOfSquares(self,n:int) -> int:
        output =0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10

        return output

class TestHappyNumber(unittest.TestCase):
    def test_happy_number(self):
        self.assertEqual(Solution().isHappy(n=19), True)
        self.assertEqual(Solution().isHappy(n=2), False)

if __name__ == '__main__':
    unittest.main()
