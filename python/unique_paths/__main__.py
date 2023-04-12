import unittest
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n 

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n - 2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
    

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().uniquePaths(3, 2), 3)

    def test_2(self):
        self.assertEqual(Solution().uniquePaths(7, 3), 28)

    def test_3(self):
        self.assertEqual(Solution().uniquePaths(3, 3), 6)

if __name__ == "__main__":
    unittest.main()