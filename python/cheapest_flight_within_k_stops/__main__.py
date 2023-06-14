from typing import List
import unittest



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0


        for i in range(k+1): 
            tmpPrices = prices.copy()

            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s]+p

            prices = tmpPrices

        
        return -1 if prices[dst] == float("inf") else prices[dst]


class Test(unittest.TestCase):
    def test(self):
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 1
        out = 200
        self.assertEqual(Solution().findCheapestPrice(n,flights,src,dst,k),out)
        n = 3
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        src = 0
        dst = 2
        k = 0
        out = 500
        self.assertEqual(Solution().findCheapestPrice(n,flights,src,dst,k),out)
        n = 5
        flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
        src = 0
        dst = 2
        k = 2
        out = 7
        self.assertEqual(Solution().findCheapestPrice(n,flights,src,dst,k),out)
        n = 5
        flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
        src = 0
        dst = 2
        k = 1
        out = 10
        self.assertEqual(Solution().findCheapestPrice(n,flights,src,dst,k),out)
        n = 5
        flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
        src = 0
        dst = 2
        k = 0
        out = -1
        self.assertEqual(Solution().findCheapestPrice(n,flights,src,dst,k),out)
        n = 5
        flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
        src = 0
        dst = 4
        k = 0
        out = 6


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)