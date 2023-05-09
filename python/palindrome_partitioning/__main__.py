from typing import List
import unittest

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        part =[]

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)

        return res


    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        return True


class Test(unittest.TestCase):

    def test(self):
        s = "aab"
        out = [["a","a","b"],["aa","b"]]
        self.assertEqual(Solution().partition(s),out)
        s = "a"
        out = [["a"]]
        self.assertEqual(Solution().partition(s),out)
        s = "ab"
        out = [["a","b"]]
        self.assertEqual(Solution().partition(s),out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)