from typing import List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src,dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)


        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):return True
                adj[src].insert(i,v)
                res.pop()
            return False
            

        dfs("JFK")

        return res
    
class Test(unittest.TestCase):
    def test_one(self):
        tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        answer = ["JFK","MUC","LHR","SFO","SJC"]
        result = Solution().findItinerary(tickets)
        self.assertEqual(answer, result)
    
    def test_two(self):
        tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        answer = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        result = Solution().findItinerary(tickets)
        self.assertEqual(answer, result)

if __name__ == "__main__":
    unittest.main()