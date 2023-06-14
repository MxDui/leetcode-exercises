import heapq
from collections import defaultdict
from typing import List
import unittest


class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


class Test(unittest.TestCase):
    def test1(self):
        obj = Twitter()
        obj.postTweet(1, 5)
        self.assertEqual(obj.getNewsFeed(1), [5])
        obj.follow(1, 2)
        obj.postTweet(2, 6)
        self.assertEqual(obj.getNewsFeed(1), [6, 5])
        obj.unfollow(1, 2)
        self.assertEqual(obj.getNewsFeed(1), [5])

    def test2(self):
        obj = Twitter()
        obj.postTweet(1, 5)
        obj.postTweet(1, 3)
        obj.postTweet(1, 101)
        obj.postTweet(1, 13)
        obj.postTweet(1, 10)
        obj.postTweet(1, 2)
        obj.postTweet(1, 94)
        obj.postTweet(1, 505)
        obj.postTweet(1, 333)
        obj.postTweet(1, 22)
        self.assertEqual(obj.getNewsFeed(1), [22, 333, 505, 94, 2, 10, 13, 101, 3, 5])
        obj.follow(1, 2)
        self.assertEqual(obj.getNewsFeed(1), [22, 333, 505, 94, 2, 10, 13, 101, 3, 5])
        obj.unfollow(1, 2)
        self.assertEqual(obj.getNewsFeed(1), [22, 333, 505, 94, 2, 10, 13, 101, 3, 5])


if __name__ == "__main__":
    unittest.main()
